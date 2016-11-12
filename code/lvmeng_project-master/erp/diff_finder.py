# encoding: utf-8


class DiffFinder(object):

    def __init__(self):
        self.diffs = {
            'delete': [],
            'add': [],
            u'\u4fee\u6539': [],
        }

    @property
    def has_changed(self):
        if self.diffs['delete'] or self.diffs['add'] or self.diffs[u'\u4fee\u6539']:
            return True
        return False

    def delete(self, key, val):
        self.diffs['delete'].append(key)

    def add(self, key, val):
        self.diffs['add'].append((key, val))

    def change(self, key, val):
        self.diffs[u'\u4fee\u6539'].append((key, val))

    def diff(self, old_data, new_data, key=None):
        if type(old_data) == dict and type(new_data) == dict:
            self.diff_dict(old_data, new_data, key)
        else:
            # if key:
                self.change(key, new_data)
            # else:
            #     self.add(key, new_data)

    def diff_dict(self, old_dict, new_dict, parent_key):
        for key in old_dict.keys():
            # if key not in new_dict:
            #     log_key = self.join_dict_and_list_key(parent_key, key)
            #     self.delete(log_key, old_dict[key])
            if old_dict[key] != new_dict[key]:
                log_key = self.join_dict_and_list_key(parent_key, key)
                self.diff(old_dict[key], new_dict[key], log_key)
            # else:
            #     pass

        for key in new_dict.keys():
            if key not in old_dict:
                log_key = self.join_dict_and_list_key(parent_key, key)
                self.add(log_key, new_dict[key])


    def diff_list(self, old_list, new_list, parent_key):
        for index, val in enumerate(old_list):
            if val not in new_list:
                log_key = self.join_dict_and_list_key(parent_key, 'index' + str(index))
                self.delete(log_key, val)

        for index, val in enumerate(new_list):
            if val not in old_list:
                log_key = self.join_dict_and_list_key(parent_key, 'index' + str(index))
                self.add(log_key, val)


    def join_dict_and_list_key(self, key1, key2):
        if key1 == None:
            #depth=0
            return key2
        else:
            return self.join_key(key1, key2)

    def join_key(self, key1, key2):
        return '.'.join([str(key1), str(key2)])

class NoChangeDiffFinder(DiffFinder):

    def __init__(self, ignore_key_list=[]):
        self.diffs = {
            'delete': [],
            'add': [],
            u'\u4fee\u6539': [],
        }
        self.ignore_key_list = ignore_key_list

    @property
    def format_diffs_str(self):
        result_list = []

        del_str_list = []
        for key, val in self.diffs[u'\u4fee\u6539']:
            if key in self.ignore_key_list:
                continue
            del_str_list.append('%s=%s'% (key, val))
        if del_str_list:
            del_str = ','.join(del_str_list)
            del_str = u'\u4fee\u6539'+'=[%s]'% del_str
            result_list.append(del_str)

        add_str_list = []
        for key, val in self.diffs['add']:
            if key in self.ignore_key_list:
                continue
            add_str_list.append('%s=%s'% (key, val))
        if add_str_list:
            add_str = ','.join(add_str_list)
            add_str = 'add=[%s]'% add_str
            result_list.append(add_str)

        return ','.join(result_list)


    @property
    def has_changed(self):
        if self.diffs['delete'] or self.diffs['add']:
            return True
        return False

    def delete(self, key, val):
        self.diffs['delete'].append((key, val))

    def change(self, key, val):
        self.diffs[u'\u4fee\u6539'].append((key, val))

    def diff(self, old_data, new_data, key=None):
        if type(old_data) == dict and type(new_data) == dict:
            self.diff_dict(old_data, new_data, key)
        else:
            if key:
                self.add(key, new_data)
                self.change(key, old_data)
            else:
                self.add(key, new_data)
