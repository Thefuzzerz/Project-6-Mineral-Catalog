from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from minerals.models import Mineral, initialize, common_attributes
import json


class MineralModelTests(TestCase):

    def mineral_creation(self,
                              category = "category",
                              cleavage = "cleavage",
                              color = "color",
                              crystal_habit = "crystal_habit",
                              crystal_symmetry = "crystal_symmetry",
                              crystal_system = "crystal_system",
                              diaphaneity = "diaphaneity",
                              formula = "formula",
                              group = "group",
                              image_caption = "image_caption",
                              image_filename = "image_filename",
                              luster = "luster",
                              mohs_scale_hardness = "mohs_scale_hardness",
                              name = "name",
                              optical_properties = "optical_properties",
                              refractive_index = "refractive_index",
                              specific_gravity = "specific_gravity",
                              streak = "streak",
                              strunz_classification = "strunz_classification",
                              unit_cell = "unit_cell"):
        return Mineral.objects.create(category = "category",
                            cleavage = cleavage,
                            color = color,
                            crystal_habit = crystal_habit,
                            crystal_symmetry = crystal_symmetry,
                            crystal_system = crystal_system,
                            diaphaneity = diaphaneity,
                            formula = formula,
                            group = group,
                            image_caption = image_caption,
                            image_filename = image_filename,
                            luster = luster,
                            mohs_scale_hardness = mohs_scale_hardness,
                            name = name,
                            optical_properties = optical_properties,
                            refractive_index = refractive_index,
                            specific_gravity = specific_gravity,
                            streak = streak,
                            strunz_classification = strunz_classification,
                            unit_cell = unit_cell
                            )

    def test_mineral_creation(self):
        mineral = self.mineral_creation()
        self.assertTrue(isinstance(mineral, Mineral))
        self.assertEqual(mineral.__str__(), mineral.name)

class InitializeTest(TestCase):
    def test_initialize(self):
        jdata=open('minerals/minerals.json')
        json_data = json.load(jdata)
        minerals = [{ "name": "Abelsonite",
                    "image_filename": "Abelsonite.jpg",
                    "image_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
                    "category": "Organic",
                    "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
                    "strunz_classification": "10.CA.20",
                    "crystal_system": "Triclinic",
                    "unit_cell": "a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
                    "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
                    "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
                    "cleavage": "Probable on {111}",
                    "mohs_scale_hardness": "2\u20133",
                    "luster": "Adamantine, sub-metallic",
                    "streak": "Pink",
                    "diaphaneity": "Semitransparent",
                    "optical_properties": "Biaxial",
                    "group": "Organic Minerals"
                    },
                    {
                    "name": "Abernathyite",
                    "image_filename": "Abernathyite.jpg",
                    "image_caption": "Pale yellow abernathyite crystals and green heinrichite crystals",
                    "category": "Arsenate",
                    "formula": "K(UO<sub>2</sub>)(AsO<sub>4</sub>)\u00b7<sub>3</sub>H<sub>2</sub>O",
                    "strunz_classification": "08.EB.15",
                    "crystal_system": "Tetragonal",
                    "unit_cell": "a = 7.176\u00c5, c = 18.126\u00c5Z = 4",
                    "color": "Yellow",
                    "crystal_symmetry": "H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
                    "cleavage": "Perfect on {001}",
                    "mohs_scale_hardness": "2.5\u20133",
                    "luster": "Sub-Vitreous, resinous, waxy, greasy",
                    "streak": "Pale yellow",
                    "diaphaneity": "Transparent",
                    "optical_properties": "Uniaxial (-)",
                    "refractive_index": "n\u03c9 = 1.597 \u2013 1.608n\u03b5 = 1.570",
                    "group": "Arsenates"}]
        initialize(json_data)
        for mineral in json_data:
            mineral_name = mineral.get("name")
            exists = Mineral.objects.filter(name=mineral_name).count()
            self.assertEqual(exists, 1)

class MineralViewsTests(TestCase):
    def setUp(self):
        minerals = [{ "name": "Abelsonite",
                    "image_filename": "Abelsonite.jpg",
                    "image_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
                    "category": "Organic",
                    "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
                    "strunz_classification": "10.CA.20",
                    "crystal_system": "Triclinic",
                    "unit_cell": "a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
                    "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
                    "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
                    "cleavage": "Probable on {111}",
                    "mohs_scale_hardness": "2\u20133",
                    "luster": "Adamantine, sub-metallic",
                    "streak": "Pink",
                    "diaphaneity": "Semitransparent",
                    "optical_properties": "Biaxial",
                    "group": "Organic Minerals"
                    },
                    {
                    "name": "Abernathyite",
                    "image_filename": "Abernathyite.jpg",
                    "image_caption": "Pale yellow abernathyite crystals and green heinrichite crystals",
                    "category": "Arsenate",
                    "formula": "K(UO<sub>2</sub>)(AsO<sub>4</sub>)\u00b7<sub>3</sub>H<sub>2</sub>O",
                    "strunz_classification": "08.EB.15",
                    "crystal_system": "Tetragonal",
                    "unit_cell": "a = 7.176\u00c5, c = 18.126\u00c5Z = 4",
                    "color": "Yellow",
                    "crystal_symmetry": "H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
                    "cleavage": "Perfect on {001}",
                    "mohs_scale_hardness": "2.5\u20133",
                    "luster": "Sub-Vitreous, resinous, waxy, greasy",
                    "streak": "Pale yellow",
                    "diaphaneity": "Transparent",
                    "optical_properties": "Uniaxial (-)",
                    "refractive_index": "n\u03c9 = 1.597 \u2013 1.608n\u03b5 = 1.570",
                    "group": "Arsenates"}]
        initialize(json_data=minerals)
        self.mineral_1 = Mineral.objects.get(name="Abelsonite")
        self.mineral_2 = Mineral.objects.get(name="Abernathyite")

    def test_home_page_view(self):
        resp = self.client.get(reverse('minerals:home_page'))
        self.assertEqual(resp.status_code, 200)

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:mineral_list', kwargs={'refine': "ALL"}))
        resp_filter = self.client.get(reverse('minerals:mineral_list', kwargs={'refine': "B"}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_filter.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['minerals'])
        self.assertIn(self.mineral_2, resp.context['minerals'])
        self.assertNotIn(self.mineral_2, resp_filter.context['minerals'])
        self.assertNotIn(self.mineral_2, resp_filter.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral_1.pk, "name": self.mineral_1.name}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral_1, resp.context['mineral'])
