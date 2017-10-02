# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OutputDirectory(Model):
    """Output directory for the job.

    :param id: The name for the output directory. It will be available for the
     job as an environment variable under AZ_LEARNING_OUTPUT_id.
    :type id: str
    :param path_prefix: The prefix path where the output directory will be
     created. NOTE: This is an absolute path to prefix. E.g.
     $AZ_LEARNING_MOUNT_ROOT/MyNFS/MyLearningLogs.
    :type path_prefix: str
    :param path_suffix: The path of the directory to create. The learning
     system will create the following directory on user's behalf:
     PathPrefix/JobID/jobVersion/directoryName, where the JobID is a unique
     name created by the Batch AI Service and jobVersion is the version of the
     job. The Batch AI Service will also populate a file under this the
     PathPrefix/JobID/jobVersion directory, which maps the directory to a job
     ARM resource ID.
    :type path_suffix: str
    :param type: An enumeration, which specifies the type of job output
     directory. Default value is Custom. The possible values are Model, Logs,
     Summary, and Custom. Users can use multiple enums for a single directory.
     Eg. outPutType='Model,Logs, Summary'. Possible values include: 'model',
     'logs', 'summary', 'custom'. Default value: "custom" .
    :type type: str or :class:`OutputType
     <azure.mgmt.batchai.models.OutputType>`
    :param create_new: True to create new directory. Default is true. If
     false, then the directory is not created and can be any directory path
     that the user specifies. Default value: True .
    :type create_new: bool
    """

    _validation = {
        'id': {'required': True},
        'path_prefix': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'path_prefix': {'key': 'pathPrefix', 'type': 'str'},
        'path_suffix': {'key': 'pathSuffix', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'create_new': {'key': 'createNew', 'type': 'bool'},
    }

    def __init__(self, id, path_prefix, path_suffix=None, type="custom", create_new=True):
        self.id = id
        self.path_prefix = path_prefix
        self.path_suffix = path_suffix
        self.type = type
        self.create_new = create_new
