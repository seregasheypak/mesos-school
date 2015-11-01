def array_to_array_of_dicts(some_array, *args, **kw):
    data = []
    for some_value in some_array:
        data.append({'host': some_value})
    return data

def get_id_element_by_value(some_array, *args, **kw):
    print "some_array : " + str(some_array)
    print "args :" + str(args)
    print "some_array.index(args[0]) + 1 " + str(some_array.index(args[0]) + 1)
    return some_array.index(args[0]) + 1

class FilterModule (object):
    def filters(self):
        return {"array_to_array_of_dicts": array_to_array_of_dicts, "get_id_element_by_value": get_id_element_by_value}
