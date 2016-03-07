import os

from VirtualObject import VirtualObject


class VirtualObjectWarehouse:
    """
    The warehouse storing all virtual object
    """

    def __init__(self, directory, prefix):
        self._filename_object_dict = self._scan_object(directory, prefix)
        self._hashcode_filename_dict = {}

    def _scan_object(self, directory, prefix):
        """
        Scan all input files whose names starting with the given prefix, create virtual object from those files and
        store them in a dictionary where keys are file names and values are the created virtual objects
        :param directory: the directory to be scanned
        :type directory: str
        :param prefix: the prefix
        :type prefix: str
        :return: a dictionary where keys are file names and values are the created virtual objects
        :rtype: dict
        """
        file_list = [f for f in os.walk(directory).next()[2] if f.startswith(prefix)]

        filename_object_dict = {}
        for file_name in file_list:
            filename_object_dict[file_name] = VirtualObject(directory + "/" + file_name)

        return filename_object_dict

    def get_virtual_object_by_filename(self, file_name):
        """
        Given a file name, return the virtual object
        :param file_name: the file name
        :type file_name: str
        :return: the virtual object
        :rtype: VirtualObject
        """
        return self._filename_object_dict[file_name]

    def update_virtual_object_hashcode(self, file_name, hashcode):
        """
        Update the hashcode (created by server) of the virtual object stored in the given file name
        :param file_name: the file name
        :type file_name: str
        :param hashcode: the hashcode generated by server
        :type hashcode: hashcode
        """
        self._hashcode_filename_dict[hashcode] = file_name

    def get_virtual_object_by_hashcode(self, hashcode):
        """
        Get the virtual object using the hashcode generated by the server
        :param hashcode: the hashcode generated by the server
        :type hashcode: hashcode
        :return: the corresponding virtual object
        :rtype: VirtualObject
        """
        file_name = self._hashcode_filename_dict[hashcode]
        return self._filename_object_dict[file_name]