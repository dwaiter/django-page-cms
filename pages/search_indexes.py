"""Django haystack `SearchIndex` module."""
from pages.models import Page, Content

from haystack.indexes import SearchIndex, CharField, DateTimeField
from haystack import site

import datetime

class PageIndex(SearchIndex):
    """Search index for pages content."""
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    url = CharField(model_attr='get_absolute_url')
    publication_date = DateTimeField(model_attr='publication_date', null=True)

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Page.objects.exclude(status=Page.DRAFT).exclude(status=Page.EXPIRED)


site.register(Page, PageIndex)

