/*
    jQuery Custom Input File Plugin - version 1.0
	Copyright 2014, Ángel Espro, www.aesolucionesweb.com.ar,
	Licence : GNU General Public License

	Site: www.aesolucionesweb.com.ar/plugins/custom-input-file
	
	You must not remove these lines. Read gpl.txt for further legal information.
*/


(function($){
/*
 * CUSTOMFILE
 */
 
// Constructor (CustomFile)
CustomFile = function(elem, options){
	this.elem = $(elem);
	this.itemFileList = [];
	
	this.defaults = {
		type 		: 'all',
		allowed		: 'all', //or array of allowed extensions. E.g. ["exe", "jpeg", "jpg"]
		notAllowed	: [],//E.g. ["exe", "jpeg", "jpg"]
		addContainerAfter : $(elem), //jQuery Object. E.g $('#my-element')
		multiple	: true,
		maxFiles	: 5, //0 = no limits
		maxMB		: 0, //0 = no limits
		maxKBperFile: 2048,
		fileWrapper	: '<div class="cif-parent"></div>', //markup or jQuery object. E.g $('#my-element')
		filePicker	: '<h3>Drop files here</h3><p>or click to select them</p><div class="cif-icon-picker"></div>',//markup or jQuery object. E.g $('#my-element')
		image : {
			crop	: false,
			preview : {
				display: true, 
				maxWidth: 300	//if cropSize were wider than maxWidth, only preview would be redimensioned (real crop area would not)
			},
			cropSize: [320,225], //[width, height]
			minSize	: [0,0], //[width, height] 0 = no limits
			maxSize : [0,0]  //[width, height] 0 = no limits
		},
		messages : {
			errorType : "File type not allowed",
			errorMaxMB : "Total weight exceeded",
			errorFileKB : "File too heavy",
			errorMaxFiles : "Maximum number of files reached",
			errorBigImage : "Image too big",
			errorSmallImage : "Image too small",
			errorOnReading : "App busy. Please, try again later.",
			errorMultipleDisable : "Drag & drop one file at a time."
		},
		popup : {
			active : true,
			autoclose : true,
			delay : 10000 //10sec
		},
		callbacks : {
			onComplete : function(app){
				//function fires when all files have already read;
			},
			beforeRead : function(file){
				//function fires every time a file is just to be read;
				//Return false if you want to stop app reading this file
			},
			onSuccess : function(item, callback){
				//function called every time a file has been successfuly read;
				//retur false for stop app reading next file. Then, you can execute callback for reading next file.
				//E.g. 
				//item.serialize(); FunctionToSend(callback); return false;
			},
			onError : function(file, msg){
				//function called every time a file has been not successfuly read;
			},
			beforeRemove : function(item){
				//function called every time an item file is been removed;
				//Here you can handle file (item.file) before removing item
			},
		}
		
		
	}
	this.settings =  $.extend(true, {}, this.defaults, options);
	
	this.status = 'stop';
	
	this.init();
}

//Methods (CustomFile)
CustomFile.prototype = {
	
	init : function(){
		var attnm = this.elem.attr("name");
		if(attnm == '') var attnm = "inputfile";
		//properties:
		this.name = (attnm.indexOf("[]", attnm - 2) === -1)? attnm+"[]" : attnm;
		this.form = this.elem.parents('form');
		this.container = $('<div class="cif-file-container cif-container-'+this.settings.type+'-type">');
		
		//minSize for images
		var image = this.settings.image;
		image.minSize = (typeof(image.minSize) !== 'object' || image.minSize.length !== 2)? [0,0] : image.minSize;
		if(image.crop){
			var minSize = [];
			for(i=0;i<image.minSize.length;i++){
				var value = (image.minSize[i]>image.cropSize[i])? image.minSize[i] : image.cropSize[i];
				minSize.push(value);
			}
			image.minSize = minSize
		}
		
		//calling methods and creating instance of File Picker
		this.setFileWrapper();
		this.appendContainer();
		this.filePicker = new FilePicker(this);
		
		//store in $.customFile Object
		$.customFile.elements.push(this); 
	},
	
	onSuccess : function(item, callback){
		this.itemFileList.push(item);
		if(this.settings.callbacks.onSuccess(item, callback) === false) return;
		callback();
	},
	onError : function(file, msg){
		this.settings.callbacks.onError(file, msg);
		var popupSet = this.settings.popup;
		if(popupSet.active)
		for(k=0;k<msg.length;k++){
			var fileExt = file.name.substr(file.name.lastIndexOf('.') + 1);
			var fileName = file.name.substr(0, file.name.lastIndexOf('.'));
			if(fileName.length > 42 ) var fileName = fileName.substr(0,40) + "...";
			msg[k] += ' ('+fileName+'.'+fileExt+')';
			$.customFile.popup.add( msg[k], popupSet.autoclose, popupSet.delay , 'error');
		}
	},
	onComplete : function(){
		this.status = "completed";
		if(this.settings.multiple){
			var response = this.checkMaxFiles()
			var popupSet = this.settings.popup;
			if(response && popupSet.active) $.customFile.popup.add( response, popupSet.autoclose, popupSet.delay , 'ok');//////////////////////////////////////////////////////////////////////////
		}else{
			if(this.itemFileList.length>1) this.itemFileList[0].destroy();
		}
		
		this.settings.callbacks.onComplete(this);
	},
	read : function(fileList, currentItem){
		var i = currentItem;

		if(i+1>fileList.length) this.status = 'completed';
	
		if(this.status === 'completed'){
			this.onComplete();
			return false;
		}
		
		var beforeRead = this.settings.callbacks.beforeRead(fileList[i]);
		if(beforeRead === false) return this.read(fileList, i+1);

		app = this;
		var response = app.checkMaxFiles(fileList[i]);
		if(typeof(response) === 'string'){
			this.onError(fileList[i],[response]);
			return this.read(fileList, i+1);
		}
			
		var msg = [];
		var checklist = ["checkFileKB", "checkFileType", "checkTotalMB"]
		
		for(j=0;j<checklist.length;j++){
			var response = app[checklist[j]](fileList[i]);
			if(response) msg.push(response)
		}
		if(msg.length>0){
			this.onError(fileList[i],msg);
			return this.read(fileList, i+1);
		}
		
		new FileItem(this, fileList, i);
	},
	
	
	appendContainer : function(){
		var sett = this.settings;
		if(sett.fileWrapper.parent().length != 0 && sett.appendAfter != this.elem){
			sett.addContainerAfter = sett.fileWrapper;
		}
		sett.addContainerAfter.after(this.container);
	},
	
	setFileWrapper : function(){
		//Edit name attr for each fileWrapper input
		var app = this;
		var fwr = this.settings.fileWrapper;
		if(typeof(fwr)==='string') this.settings.fileWrapper = $(fwr);
		this.settings.fileWrapper = $('<div>', {class: "cif-file-row"}).append(this.settings.fileWrapper);
		var fwr = this.settings.fileWrapper;
		fwr.find(':input').each(function(index){
			var $this = $(this);
			var attnm = $this.attr("name");
			if(!attnm) var attnm = app.name.substr(0, app.name.indexOf("[]", -2))+"-"+index;
			if(attnm.indexOf("[]", - 2) === -1){
				$this.attr("name",attnm+"[]");
			}
		});
		//prepare fileWrapper's children
		if(fwr.find('.cif-img').length==0 && this.settings.type == 'image'){
			var parent = fwr.find('.cif-parent');
			if(parent.length===0){
				var $img = fwr.find('img');
				var parent = $('<div>', {class: 'cif-parent'});
				parent.append($img);
				fwr.append(parent);
			}
			if(parent.find('img').length === 0) parent.append('<img>')
			parent.find('img').addClass("cif-img");
		}
		if(fwr.find('.cif-parent').length==0){
			fwr.prepend('<div class="cif-parent"></div>');
		}
	},
	
	//Cheking files...
	checkFileKB : function(file){
		if(file.size>this.settings.maxKBperFile*1024 && this.settings.maxKBperFile!=0){
			var msg = this.settings.messages.errorFileKB;
		}
		return msg;
	},
	
	checkFileType : function(file){
		var ext = file.name.substr(file.name.lastIndexOf('.') + 1);
		var ext = ext.toLowerCase();
		var imageCropAllowed = ["jpeg", "jpg", "png"]
		if((this.settings.type == 'image' && this.settings.image.crop && imageCropAllowed.indexOf(ext) == -1)
			|| (this.settings.type == 'image' && !file.type.match(/image\//))
			|| (this.settings.allowed != 'all' && this.settings.allowed.indexOf(ext) == -1)
			|| (this.settings.notAllowed.indexOf(ext) != -1))
		{
			var msg = this.settings.messages.errorType;
		}
		return msg;
	},
	
	checkMaxFiles : function(file){
		if(this.settings.maxFiles<=this.itemFileList.length && this.settings.maxFiles){
			var msg = this.settings.messages.errorMaxFiles;
			this.filePicker.btn.addClass('inactive');
		}else{
			this.filePicker.btn.removeClass('inactive');
		}
		return msg;
	},
	
	checkTotalMB : function(file){
		var fileSize = (typeof(file)!=='undefined')? file.size : 0;
		var totalSize = 0;
		for(var obj in this.itemFileList){
			totalSize += this.itemFileList[obj].file.size;
		}
		if(fileSize+totalSize>this.settings.maxMB*1024*1024 && this.settings.maxMB!=0){
			var msg = this.settings.messages.errorMaxMB;
		}
		return msg;
	},
	
	checkImageSize : function(img, file){
		var stt = this.settings.image

		if((stt.minSize[0] && img.width<stt.minSize[0]) || (stt.minSize[1] && img.height<stt.minSize[1]) ){
			var msg = this.settings.messages.errorSmallImage;
			if(stt.minSize[0]) msg += ' Ancho mínimo:'+stt.minSize[0]+'px.';
			if(stt.minSize[1]) msg += ' Alto mínimo: '+stt.minSize[1]+'px.';
		}
		if((stt.maxSize[0] && img.width>stt.maxSize[0]) || (stt.maxSize[1] && img.height>stt.maxSize[1]) ){
			var msg = this.settings.messages.errorBigImage;
			if(stt.maxSize[0]) msg += ' Ancho máximo:'+stt.maxSize[0]+'px.';
			if(stt.maxSize[1]) msg += ' Alto máximo: '+stt.maxSize[1]+'px.';
		}
		return msg;
	},
}

/*
 * FOTOPICKER
 */
 
// Constructor (FilePicker)
FilePicker = function(app){
	this.btn = $('<div class="cif-file-picker"></div>').append(app.settings.filePicker);
	this.init(app);
}

// Methods (FilePicker)
FilePicker.prototype = {
		
	init : function(app){
		var multiple = (app.settings.multiple || app.elem.attr("multiple") == "multiple")? 'multiple="multiple"' : ' ';
		this.inputHidden = $('<input type="file" '+multiple+'/>');
		app.elem.after(this.btn);
		var elem = app.elem.clone();
		app.elem.detach();
		app.elem = elem;
		
		//set className
		this.btn.addClass("cif-pkr-"+app.elem.attr("name"));
		
		var btn = this.btn;
		var inputHidden = this.inputHidden;
		
		//events
		inputHidden.change(function(){
			var popupSet = app.settings.popup;
			if(app.status == 'reading') return $.customFile.popup.add( app.settings.messages.errorOnReading, popupSet.autoclose, popupSet.delay , 'error');//return if app is reading
			//Read Files
			$.customFile.popup.close();
			fileList = $(this)[0].files;
			app.status = 'reading';
			app.read(fileList, 0);
		});
		
		btn.on({
			click : function(){
				 if(!$(this).is('.inactive')) inputHidden.click();
				 return false;
			},
			dragover: function(e){
				e = e || window.event;
				e.preventDefault();
				if($(this).is('.inactive')) e.dataTransfer.dropEffect =	'none';
				btn.addClass('dragover');
				return false;
			},
			dragleave: function(e){
				btn.removeClass('dragover');
				return false;
			},
			drop : function(e){
				e = window.event;
				e.preventDefault();
				btn.removeClass('dragover');
				
				var popupSet = app.settings.popup;
				if(app.status == 'reading') return $.customFile.popup.add( app.settings.messages.errorOnReading, popupSet.autoclose, popupSet.delay , 'error');//return if app is reading
				//Read Files.
				$.customFile.popup.close();
				var fileList =  e.dataTransfer.files;
				if(fileList.length>1 && !app.settings.multiple) return $.customFile.popup.add( app.settings.messages.errorMultipleDisable, popupSet.autoclose, popupSet.delay , 'error');//return if app is reading
				app.status = 'reading';
				app.read(fileList, 0);
			}
		});

	},
	
};

/*
 * FILE
 */

FileItem = function(app, fileList, currentItem){
	this.file = fileList[currentItem];
	this.app = app;
	this.fileList = fileList;
	this.currentItem = currentItem;
	this.init();
}
FileItem.prototype = {
	init : function(){
		
		this.jcropObj = null;
		this.node = this.app.settings.fileWrapper.clone();
		this.img = null;
		this.btnClose = $('<div class="cif-close" title="Remove">close</div>');
		this.btnClose.click(function(){
			fileObj.destroy();
		});
		this.fr = new FileReader;
		
		var	fr = this.fr;
		var	app = this.app;
		var fileObj = this;
		var fileList = this.fileList;
		var currentItem = this.currentItem;
		
		var callback = function(){
			app.onSuccess(fileObj, function(){
				app.read(fileList, currentItem+1);
			}); 
			// delete temp properties for clearer future use of current object
			delete fileObj.fr;
			delete fileObj.fileList; 
			delete fileObj.currentItem; 
		}
		
		fr.onload = function(){
			switch(app.settings.type){
				case "image" : 
					fileObj.readImage(callback);
					break;
				default :
					fileObj.readAllTypes(callback);
					break;
			}
		}
		fr.readAsDataURL(this.file);
	},
	
	destroy : function(){
		this.app.settings.callbacks.beforeRemove(this);
		if(this.node) this.node.remove();
		var i = this.app.itemFileList.indexOf(this);
		this.app.itemFileList.splice(i, 1);
		this.app.checkMaxFiles();
	},
	serialize : function(){
		return $.customFile.serialize([{key: this.app.name, value: this.file}]);
	},
	readImage : function(callback){
		var fileObj = this;
		var fr = this.fr;
		var app = this.app;
		var imgNode = fileObj.node.find("img.cif-img");
		fileObj.img = new Image;
		fileObj.img.src = fr.result;
		fileObj.img.onload = function(){
			msg = app.checkImageSize(fileObj.img, fileObj.file);
			if(msg){
				app.onError(fileObj.file, [msg]);
				return app.read(fileObj.fileList, fileObj.currentItem+1);
			}

			imgNode.attr("src", fr.result);
			imgNode.parent().prepend(fileObj.btnClose);
			
			//Append node to container
			app.container.append(fileObj.node); 
						
			if(app.settings.image.crop === true){
				fileObj.jcropObj = fileObj.initJcrop(app.settings.image, imgNode.parent(), fileObj.img);
			}
			//Callback
			callback();
			
		}
		
	},
	
	readAllTypes : function(callback){
		fileObj = this;
		var parent = fileObj.node.find('.cif-parent');
		var FileExt = fileObj.file.name.substr(fileObj.file.name.lastIndexOf('.') + 1);
		var FileName = fileObj.file.name.substr(0, fileObj.file.name.lastIndexOf('.'));
		if(FileName.length > 42 ) var FileName = FileName.substr(0,40) + "...";
		var fileSize = (fileObj.file.size < 102400)? (fileObj.file.size/1024).toFixed(2) : Math.round(fileObj.file.size/1024); //display two different formats, if is less than 100KB or heavier
		parent.append($('<div class="cif-all-type">'+FileName+'.'+FileExt+' <span class="cif-file-size">('+fileSize+'KB)</span><div>')).append(fileObj.btnClose);
		this.app.container.append(fileObj.node)
		callback();
	},
		
	initJcrop : function(options, parent, img){
		var jcrop_api,
		boundx,
		boundy;
		
		//if preview is turn on
		if(options.preview.display){
			prevMaxWidth = options.preview.maxWidth;
			prevSize = (options.cropSize[0]>prevMaxWidth)? [prevMaxWidth, options.cropSize[1]/options.cropSize[0]*prevMaxWidth] : options.cropSize; 
			parent.append('<div class="preview-pane" style="width:'+prevSize[0]+'px;height:'+prevSize[1]+'px;"><div class="preview-container" style="width:'+prevSize[0]+'px;height:'+prevSize[1]+'px; overflow:hidden"><img src="'+img.src+'" class="jcrop-preview im-prv" /></div></div> '
						+'<input type="hidden" class="jcropx" name="x[]" /><input type="hidden" class="jcropy" name="y[]" /><input type="hidden" class="jcropw" name="w[]" /><input type="hidden" class="jcroph" name="h[]" />');
			parent.css("min-height", prevSize[1]+20+"px");
		}
		
		// Grab some information about the preview pane
		var $preview = parent.find('.preview-pane'),
		$pcnt = $preview.find('.preview-container'),
		$pimg = $preview.find('.preview-container img'),
		
		xsize = $pcnt.width(),
		ysize = $pcnt.height();
		
		api = parent.find('.cif-img').Jcrop({
			keySupport: false,
			onChange: updatePreview,
			onSelect: updatePreview,
			aspectRatio: options.cropSize[0]/options.cropSize[1],
			minSize : options.cropSize,
			trueSize: [img.width,img.height]
		},function(){
			// Use the API to get the real image size
			var bounds = this.getBounds();
			boundx = bounds[0];
			boundy = bounds[1];
			jcrop_api = this;
			jcrop_api.animateTo([0,0,options.cropSize[0]]);
			// Move the preview into the jcrop container for css positioning
			$preview.appendTo(jcrop_api.ui.holder);
		});
	
		function updatePreview(c){
		  if (parseInt(c.w) > 0 && options.preview.display){
			var rx = xsize / c.w;
			var ry = ysize / c.h;
	
			$pimg.css({
			  width: Math.round(rx * boundx) + 'px',
			  height: Math.round(ry * boundy) + 'px',
			  marginLeft: '-' + Math.round(rx * c.x) + 'px',
			  marginTop: '-' + Math.round(ry * c.y) + 'px'
			});
		  }
		  updateCoords(c);
		  
		};
		function updateCoords(c){
		  parent.find('.jcropx').val(c.x);
		  parent.find('.jcropy').val(c.y);
		  parent.find('.jcropw').val(c.w);
		  parent.find('.jcroph').val(c.h);
		}
		return jcrop_api;
	}
}


/*
 *
 *Public Static methods (CustomFile)
 *
 */
 
$.customFile = {
	
	elements : [],
	
	/*
	 * Get Elements: form, inputs or pseudoInputs file
	 */
	getElements : function(selector){
		//it returns an array of object. Argument: ".myform, #myinput, textarea, input, name-of-my-custom-input-file"
		var elements = [];
		var selector = selector.split(",");
		var el = $.customFile.elements;
		
		for(k=0; k<selector.length; k++){
			selector[k] = selector[k].trim()
			for(i=0; i<el.length; i++){
				if(el[i].name === selector[k]+"[]" || el[i].name === selector[k]) 
					elements.push({type: "pseudoinput", obj: el[i]});
				if($(selector[k]).is('form')){
					$(selector[k]).each(function(){
						elements.push({type: "form", obj:  $(this), pseudoChild : (el[i].form[0] === $(this)[0])});
					});
				}
				if($(selector[k]).is(':input')){
					$(selector[k]).not(':submit').each(function(){
						elements.push({type: "input", obj: $(this)});
					});
				}
			}
		}
		
		//Remove duplicates. Store duplicate elem in indexToRemove, and then copy no duplicate elems into a new array (var result)
		var indexToRemove = []
		for(i=0; i<elements.length; i++){
			if(indexToRemove.indexOf(i) !== -1) continue;
			
			for(j=0; j<elements.length; j++){
				if(j === i || indexToRemove.indexOf(j) !== -1) continue;
				switch(elements[i].type){
					case "form" : 
						var el = elements[i].obj[0];
						if(el ===  elements[j].obj[0]
						 ||(elements[j].type === "pseudoinput" && el == elements[j].obj.form[0])
						 || (elements[j].type === "input" && el == elements[j].obj.parents('form')[0])
						) {
							indexToRemove.push(j);
						}
					break;
					
					case "input" :
						var el = elements[i].obj[0];
						if(el ===  elements[j].obj[0])
						 	indexToRemove.push(j);
					break;
					
					case "pseudoinput" :
						var el = elements[i].obj.name;
						if(el ===  elements[j].obj.name || el+"[]" === elements[j].obj.name)
						 	indexToRemove.push(j);
					break;
				}
			}
			
		}

		var result =[];
		for(i=0;i<elements.length; i++){
			if(indexToRemove.indexOf(i) === -1) result.push(elements[i]);
		}
		return result;
	},	


	/*
	 *Serialize form, inputs or pseudoInputs file
	 */
	serialize : function(elements){
		formData = null;
		
		if(typeof(elements) === 'object'){  // e.g. $.customFile.serialize([{key: "myFile", value: myFile},{key: "myInputText", value: "text to send"}]);
			formData = formData || new FormData();
			if(!elements.length) var elements = [elements]
			for(j=0;j<elements.length;j++){
				if(elements[j].hasOwnProperty("key") && elements[j].hasOwnProperty("value")){
					formData.append(elements[j].key, elements[j].value);
				}
			}
			
		}
		if(typeof(elements) === 'string'){ // e.g. $.customFile.serialize("#myInput, myPseudoInputFileName, etc"); or just $.customFile.serialize("#myForm");
			elements = this.getElements(elements);
			//elements = (arguments.length>0)? arguments : [$('form')]; //Default all forms
			
			for(j=0;j<elements.length;j++){
				formData = formData || new FormData();
				var elem = elements[j];
			
				switch(elem.type){
					case 'pseudoinput':
						$.each(elem.obj.itemFileList, function(index, element){
							formData.append(elem.obj.name, element.file);
						});
						break;
						
					case "form":
						//For each real input
						$.each(elem.obj.find(':input'), function(){
							if($(this).not(':submit'))
								formData.append($(this).attr("name"), $(this).val());
						});
						//For each Pseudoinput File
						var app = elem.obj.data("appCustomFile");
						if(typeof(app) == "undefined"){
							elem.obj.data("appCustomFile", []);
						}
						$.each(app, function(){
							appThis = this;
							$.each(appThis.itemFileList, function(index, element){
								formData.append(appThis.name, element.file);
							});
						});
						break;
						
					case "input" :
						formData.append(elem.obj.attr("name"), elem.obj.val());
						break;
	
				}
			}
		}
		return formData //return null if there are no elements to serialize

	},
	
	
	/*
	 * Send form, input or file
	 * E.g $.customFile.ajax('form') // $.customFile.ajax('form', {progress : false}) // $.customFile.ajax(myItem, {url : actionForm}) // 
	 */
	ajax : function(el, options){
		
		if(typeof(el) === 'string'){
			var element = this.getElements(el)[0];
			switch(element.type){
				case "form": 
					var action = element.obj.attr("action"); 
					break;
				case "input":
					var action = element.obj.parents("form").attr("action"); 
					break;
				case "pseudoinput":
					var action = element.obj.form.attr("action"); 
					break;
			}
			var formData = $.customFile.serialize(el); //Serilize element
		}
		if(typeof(el) === 'object' && el instanceof FileItem){
			var formData = el.serialize(); //Serialize file
			var action = el.app.form.attr("action"); 
		}

		var defaults = {
			cache: false,
			contentType: false,
			data: formData,
			processData: false,
			url: action,
			type: 'POST',
			progressBar : {
				active : true,
				markup : '<div class="cf-progressbar-wr"><div class="cf-progressbar"><span width="0"></span></div></div>',
				appendTo : $('body'),
				removeAfterComplete : true,
				node : null
			},
			progress : function(e, total, position, percent){
				this.progressBar.node.find("span").width(percent+'%');
			},

			xhr: function(){
				var ax = this;
				var xhr = $.ajaxSettings.xhr() ;
				xhr.upload.onprogress = function(e){
					var e = e || window.event;
					var position = e.position || e.loaded;
					var total = e.totalSize || e.total;
					var percent = ((e.loaded/e.total)*100)+"";
					ax.progress(e, total, position, percent);
				} ;
				xhr.upload.onload = function(){ 
					ax.progressBar.node.find("span").width('100%');
					if(ax.progressBar.removeAfterComplete)
					ax.progressBar.node.fadeOut(function(){
						$(this).remove();
					});
				} ;
				return xhr ;
			},
			 
			beforeSend : function(){},
			complete : function(){},
			success: function(xml){
				//console.log(xml);
			},
		}
		var settings =  $.extend(true, {}, defaults, options);
		
		//append progressbar
		if(!settings.progressBar.active) settings.progress = function(){};
		settings.progressBar.node = $(settings.progressBar.markup);
		var settBefore = settings.beforeSend;
		if(settings.progressBar.active){
			settings.beforeSend = function(){
				settBefore();
				settings.progressBar.appendTo.append(settings.progressBar.node);
			};
		}
		
		//Call jQuery Ajax function
		$.ajax(settings);
	},
	
	/*
	 * Validate. On Construction
	 */
	validate : function(elements, options){
		//do some stuff  with options, like validate email, telephone, not empty, callbacks, 
		//and return object {elementNoPass: [{typeOfError: 'tel', elem : element}/*elements that no pass*/], elementPass: [/*elements that pass*/], pass: boolean}
		elements = this.getElements(elements);
		for(j=0;j<elements.length;j++){
			el = elements[j];
			switch(el.type){
				case "form" : 
					//
				break;
				
				case "input" :
					//
				break;
				
				case "pseudoinput" :
					//
				break;
			}
		}
		//
	},
	
	popup :   {
		wrapper : $('<div id="cif-msg-wr"><div class="cif-msg-close">close</div></div>'),
	
		open : function(){
			var popup = this;
			this.wrapper.find('.cif-msg-close').click(function(){
				popup.close()
			});
			$('body').append(popup.wrapper);
		},
		add : function(msg, autoclose, delay, type){
			//if(!autoclose) autoclose = true; //default
			if(!delay) delay = 3000;		 //default
			switch(type){
				case "error" :
					var icon = '<span class="cif-msg-icon cif-msg-icon-error"></span>';
					break;
				case "ok" :
					var icon = '<span class="cif-msg-icon cif-msg-icon-ok"></span>';
					break;
				default :
					var icon = '';
			}
			
			var popup = this;
			if($('body').find(popup.wrapper).length<1) popup.open();
			this.wrapper.append('<div class="cif-msg">'+icon+msg+'</div>');
			if(typeof(fftimeout)!== 'undefined') clearTimeout(fftimeout);

			if(autoclose) 
				fftimeout = setTimeout(function(){
					popup.close();
				}, delay);
		},
		close : function(){
			this.wrapper.find(".cif-msg").remove();
			this.wrapper.detach();
		}
	}
}



//jQuery Plugin
$.fn.customFile = function(options){
		
	return this.each(function(){
		var element = $(this);
		var tagName = element[0].tagName.toLowerCase();

		if(tagName == 'input'){
			// Call constructor
			var customFile = new CustomFile(this, options);
			
			var prop = customFile.form
			
			//Store plugin also in data form
			if(typeof(customFile.form.data("appCustomFile")) != "undefined"){
				var formData = customFile.form.data("appCustomFile");
				formData.push(customFile);
			}else{
				var formData = new Array(customFile);
			}
			customFile.form.data("appCustomFile", formData);
		}
	});
};
   
   
})(jQuery);