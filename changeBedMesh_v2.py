# Cura PostProcessingPlugin
# Author:   Jumbo125
# Date:     22.05.2021

# Description:  This plugin change mesh bed value

import re  # To perform the search and replace.

from ..Script import Script


class changeBedMesh(Script):

    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Change Bed Mesh",
            "key": "changeBedMesh",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "save_in_epprom":
                {
                    "label": "Save changes in EPPROM",
                    "description": "When enabled, the settings will be save in the EPPROM",
                    "type": "bool",
                    "default_value": false
                },
                "set_all_same":
                {
                    "label": "Same Value",
                    "description": "If enabled, change all Points which the same Value",
                    "type": "bool",
                    "default_value": false
                },
                "allvalue":
                {
                    "label": "Value for all Points",
                    "description": "Value for all Points",
                    "type": "str",
                    "enabled": "set_all_same",
                    "default_value": ""
                },
                "set_each_other":
                {
                    "label": "Each other",
                    "description": "If enabled, change each other Points with other default",
                    "type": "bool",
                    "default_value": false
                },
                "I0J0":
                {
                    "label": "I0 J0",
                    "description": "I0J0 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I1J0":
                {
                    "label": "I1 J0",
                    "description": "I1J0 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },   
                "I2J0":
                {
                    "label": "I2 J0",
                    "description": "I2J0 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I3J0":
                {
                    "label": "I3 J0",
                    "description": "I3J0 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I4J0":
                {
                    "label": "I4 J0",
                    "description": "I4J0 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I0J1":
                {
                    "label": "I0 J1",
                    "description": "I0J1 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I1J1":
                {
                    "label": "I1 J1",
                    "description": "I1J1 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I2J1":
                {
                    "label": "I2 J1",
                    "description": "I2J1 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I3J1":
                {
                    "label": "I3 J1",
                    "description": "I3J1 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I4J1":
                {
                    "label": "I4 J1",
                    "description": "I4J1 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I0J2":
                {
                    "label": "I0 J2",
                    "description": "I0J2 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }, 
                "I1J2":
                {
                    "label": "I1 J2",
                    "description": "I1J2 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I2J2":
                {
                    "label": "I2 J2",
                    "description": "I2J2 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I3J2":
                {
                    "label": "I3 J2",
                    "description": "I3J2 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I4J2":
                {
                    "label": "I4 J2",
                    "description": "I4J2 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I0J3":
                {
                    "label": "I0 J3",
                    "description": "I0J3 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I1J3":
                {
                    "label": "I1 J3",
                    "description": "I1J3 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I2J3":
                {
                    "label": "I2 J3",
                    "description": "I2J3 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I3J3":
                {
                    "label": "I3 J3",
                    "description": "I3J3 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I4J3":
                {
                    "label": "I4 J3",
                    "description": "I4J3 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I0J4":
                {
                    "label": "I0 J4",
                    "description": "I0J4 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I1J4":
                {
                    "label": "I1 J4",
                    "description": "I1J4 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I2J4":
                {
                    "label": "I2 J4",
                    "description": "I2J4 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I3J4":
                {
                    "label": "I3 J4",
                    "description": "I3J4 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                },
                "I4J4":
                {
                    "label": "I4 J4",
                    "description": "I4J4 Value",
                    "type": "str",
                    "enabled": "set_each_other",
                    "default_value": ""
                }
            }
        }"""

    def execute(self, data):
        I0J0 = "M421 I0 J0 Q" + self.getSettingValueByKey("I0J0")
        I1J0 = "M421 I1 J0 Q" + self.getSettingValueByKey("I1J0")
        I2J0 = "M421 I2 J0 Q" + self.getSettingValueByKey("I2J0")
        I3J0 = "M421 I3 J0 Q" + self.getSettingValueByKey("I3J0")
        I4J0 = "M421 I4 J0 Q" + self.getSettingValueByKey("I4J0")
        I0J1 = "M421 I0 J1 Q" + self.getSettingValueByKey("I0J1")
        I1J1 = "M421 I1 J1 Q" + self.getSettingValueByKey("I1J1")
        I2J1 = "M421 I2 J1 Q" + self.getSettingValueByKey("I2J1")
        I3J1 = "M421 I3 J1 Q" + self.getSettingValueByKey("I3J1")
        I4J1 = "M421 I4 J1 Q" + self.getSettingValueByKey("I4J1")
        I0J2 = "M421 I0 J2 Q" + self.getSettingValueByKey("I0J2")
        I1J2 = "M421 I1 J2 Q" + self.getSettingValueByKey("I1J2")
        I2J2 = "M421 I2 J2 Q" + self.getSettingValueByKey("I2J2")
        I3J2 = "M421 I3 J2 Q" + self.getSettingValueByKey("I3J2")
        I4J2 = "M421 I4 J2 Q" + self.getSettingValueByKey("I4J2")
        I0J3 = "M421 I0 J3 Q" + self.getSettingValueByKey("I0J3")
        I1J3 = "M421 I1 J3 Q" + self.getSettingValueByKey("I1J3")
        I2J3 = "M421 I2 J3 Q" + self.getSettingValueByKey("I2J3")
        I3J3 = "M421 I3 J3 Q" + self.getSettingValueByKey("I3J3")
        I4J3 = "M421 I4 J3 Q" + self.getSettingValueByKey("I4J3")
        I0J4 = "M421 I0 J3 Q" + self.getSettingValueByKey("I0J3")
        I1J4 = "M421 I1 J3 Q" + self.getSettingValueByKey("I1J3")
        I2J4 = "M421 I2 J3 Q" + self.getSettingValueByKey("I2J3")
        I3J4 = "M421 I3 J3 Q" + self.getSettingValueByKey("I3J3")
        I4J4 = "M421 I4 J3 Q" + self.getSettingValueByKey("I4J3")

        if self.getSettingValueByKey("set_all_same"):
            I0J0 = "M421 I0 J0 Q" + self.getSettingValueByKey("allvalue")
            I1J0 = "M421 I1 J0 Q" + self.getSettingValueByKey("allvalue")
            I2J0 = "M421 I2 J0 Q" + self.getSettingValueByKey("allvalue")
            I3J0 = "M421 I3 J0 Q" + self.getSettingValueByKey("allvalue")
            I4J0 = "M421 I4 J0 Q" + self.getSettingValueByKey("allvalue")
            I0J1 = "M421 I0 J1 Q" + self.getSettingValueByKey("allvalue")
            I1J1 = "M421 I1 J1 Q" + self.getSettingValueByKey("allvalue")
            I2J1 = "M421 I2 J1 Q" + self.getSettingValueByKey("allvalue")
            I3J1 = "M421 I3 J1 Q" + self.getSettingValueByKey("allvalue")
            I4J1 = "M421 I4 J1 Q" + self.getSettingValueByKey("allvalue")
            I0J2 = "M421 I0 J2 Q" + self.getSettingValueByKey("allvalue")
            I1J2 = "M421 I1 J2 Q" + self.getSettingValueByKey("allvalue")
            I2J2 = "M421 I2 J2 Q" + self.getSettingValueByKey("allvalue")
            I3J2 = "M421 I3 J2 Q" + self.getSettingValueByKey("allvalue")
            I4J2 = "M421 I4 J2 Q" + self.getSettingValueByKey("allvalue")
            I0J3 = "M421 I0 J3 Q" + self.getSettingValueByKey("allvalue")
            I1J3 = "M421 I1 J3 Q" + self.getSettingValueByKey("allvalue")
            I2J3 = "M421 I2 J3 Q" + self.getSettingValueByKey("allvalue")
            I3J3 = "M421 I3 J3 Q" + self.getSettingValueByKey("allvalue")
            I4J3 = "M421 I4 J3 Q" + self.getSettingValueByKey("allvalue")
            I0J4 = "M421 I0 J3 Q" + self.getSettingValueByKey("allvalue")
            I1J4 = "M421 I1 J3 Q" + self.getSettingValueByKey("allvalue")
            I2J4 = "M421 I2 J3 Q" + self.getSettingValueByKey("allvalue")
            I3J4 = "M421 I3 J3 Q" + self.getSettingValueByKey("allvalue")
            I4J4 = "M421 I4 J3 Q" + self.getSettingValueByKey("allvalue")

        new_mesh = I0J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J4 + " ;change Mesh Bed Point by Jumbo125"

        if self.getSettingValueByKey("save_in_epprom"):
            new_mesh = I0J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J0 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J1 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J2 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J3 + " ;change Mesh Bed Point by Jumbo125 \n" + I0J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I1J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I2J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I3J4 + " ;change Mesh Bed Point by Jumbo125 \n" + I4J4 + " ;change Mesh Bed Point by Jumbo125 \nM500"

        search_string = "M420 S1"

        replace_string = "M420 S1 \n" + new_mesh

        for layer_number, layer in enumerate(data):
            data[layer_number] = re.sub(search_string, replace_string, layer)  # Replace all.

        return data