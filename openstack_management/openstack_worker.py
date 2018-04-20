class OpenStackTasks():
    def get_vms(self):
        pass
    def get_volumes(self):
        pass
    def get_images(self):
        pass
    def get_containers(self):
        pass
    def check_services(self):
        """
        Check openstack services list to determined which data will
        collected. return a list
        """
        return avaliavle_serivce
    def get_data(self, service):
        """
        According service_list to get data from openstack
        return a success or fail
        """
        return data
    def save_data(self, avaliavle_services, dataset):
        """
        save all validated data into db
        """
        return ok_or_fail


    def create_client(self):
        """
        Create openstack client instance prepare get data
        return client or error
        """
    def get_auth(self):
        """
        get_token
        """
    
    def delete_old_data(self, data):
        """
        Delete archive data
        """

    def archive_old_data(self):
        """
        If new data not include this data then set it to archived
        """
