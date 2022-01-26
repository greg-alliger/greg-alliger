"""
Model exported as python.
Name : Add_SABs_Fields
Group : 
With QGIS : 32202
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Add_sabs_fields(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('SABBoundary', 'SAB Boundary', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Fields_added', 'fields_added', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(11, model_feedback)
        results = {}
        outputs = {}

        # gid
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'gid',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Integer
            'INPUT': parameters['SABBoundary'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Gid'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # ogc_fid
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'ogc_fid',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Integer
            'INPUT': outputs['Gid']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Ogc_fid'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # ncessch
        alg_params = {
            'FIELD_LENGTH': 20,
            'FIELD_NAME': 'ncessch',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Ogc_fid']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Ncessch'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # schnam
        alg_params = {
            'FIELD_LENGTH': 255,
            'FIELD_NAME': 'schnam',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Ncessch']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Schnam'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # gslo
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'gslo',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Schnam']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Gslo'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # gshi
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'gshi',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Gslo']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Gshi'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # defacto
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'defacto',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Gshi']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Defacto'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # stabbrev
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'stabbrev',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Defacto']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Stabbrev'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # openenroll
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'openenroll',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Stabbrev']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Openenroll'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # level
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'level',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Openenroll']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Level'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # srcname
        alg_params = {
            'FIELD_LENGTH': 255,
            'FIELD_NAME': 'srcname',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # String
            'INPUT': outputs['Level']['OUTPUT'],
            'OUTPUT': parameters['Fields_added']
        }
        outputs['Srcname'] = processing.run('native:addfieldtoattributestable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Fields_added'] = outputs['Srcname']['OUTPUT']
        return results

    def name(self):
        return 'Add_SABs_Fields'

    def displayName(self):
        return 'Add_SABs_Fields'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Add_sabs_fields()
