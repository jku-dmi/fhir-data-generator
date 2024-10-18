import unittest


from generators.patient_tests import TestGeneratePatient
from generators.procedure_tests import TestGenerateProcedure
from generators.organization_tests import TestGenerateOrganization
from generators.episode_of_care_tests import TestGenerateEpisodeOfCare
from generators.encouter_tests import TestGenerateEncounter
from generators.condition_tests import TestGenerateCondition
from generators.medication_statement_tests import TestGenerateMedicationStatement
from generators.medication_tests import TestGenerateMedication


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGeneratePatient))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateProcedure))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateOrganization))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateEpisodeOfCare))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateEncounter))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateCondition))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateMedicationStatement))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGenerateMedication))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
