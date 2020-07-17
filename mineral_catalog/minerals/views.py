"""Views for minerals application."""

from django.shortcuts import get_object_or_404, render

from minerals.models import Mineral, common_attributes


def home_page(request):
    """Home page view."""
    return render(request, 'homepage.html')

def mineral_list(request, refine):
    """View for all minerals."""
    refine = str(refine)
    if refine == "ALL":
        minerals = Mineral.objects.all().order_by('name') # pylint: disable=E1101
    else:
        minerals = Mineral.objects.all().order_by('name').filter(name__startswith=refine) # pylint: disable=E1101
    alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z", "ALL")
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals,
                   'alphabet': alphabet,
                   'refine': refine
                   })

def mineral_detail(request, pk, name): # pylint: disable=C0103, W0613
    """View for specific mineral based on selection."""
    mineral = get_object_or_404(Mineral, pk=pk)
    def check_attr(mineral):
        """Function to filter blank attributes."""
        mineral = Mineral.objects.get(pk=mineral.pk) # pylint: disable=E1101
        invalid = ""
        valid_attr = []
        attributes = common_attributes()
        for attribute in attributes:
            value = getattr(mineral, attribute[0])
            if value not in invalid:
                attribute = attribute[0].capitalize()
                valid_attr.append([attribute, value])
        return valid_attr
    attributes = check_attr(mineral)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral':mineral,
                   'attributes':attributes
                  })
