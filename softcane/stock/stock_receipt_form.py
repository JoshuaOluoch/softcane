from .models import StockArticleReceipt, StockArticleReceiptItem

#rom .models import Profile, FamilyMember
from django.forms import ModelForm, inlineformset_factory



class StockArticleReceiptItemForm(ModelForm):
    class Meta:
        model = StockArticleReceiptItem
        exclude = ()

StockArticleReceiptItemFormSet = inlineformset_factory(StockArticleReceipt, StockArticleReceiptItem,
                                           form=StockArticleReceiptItemForm, extra=1, can_delete=True,fk_name='receipt_header_id')


