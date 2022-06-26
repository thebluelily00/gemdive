from django.conf import settings
from django.db import models
from django.utils import timezone

class Piece(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    smallbusiness = models.BooleanField()
    image = models.ImageField(upload_to='images/pieces')
    link = models.CharField(max_length=5000)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    origin_city = models.CharField(max_length=200)
    origin_state = [('AL',  'Alabama'), ('AK','Alaska'), ('AZ','Arizona'), ('AR','Arkansas'), ('AS', 'American Samoa'), ('CA', 'California'), ('CO', 'Colorado '), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('CM', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island '), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),('na','NA')]
    origin_country = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    jewelry_type = [
        ('Earrings', (
            ('studs','Studs'),
            ('o-hugs','Open huggies'),
            ('hugs','Huggies'),
            ('hoops','Hoops'),
            ('dangle','Dangle'),
            ('threaders','Threaders'),
            ('winders','Winders'),
            ('cuffs','Ear cuffs'),
        )),
        ('Necklaces',(
            ('chain','Chain'),
            ('sat','Satellite'),
            ('pen','Pendant'),
            ('bead','Beaded'),
        )),
        ('Bracelets',(
            ('chain','Chain'),
            ('sat','Satellite'),
            ('sol','solitaire'),
            ('bead','Beaded'),
            ('wov','Woven'),
        )),
        ('Rings',(
            ('wire','Wire'),
            ('bead','Beaded'),
            ('chain','Chain'),
            ('dainty','Dainty'),
            ('state','Statement'),
            ('pave','Pave'),
            ('sol','Solitaire'),
        )),
        ('Anklets',(
            ('chain','Chain'),
            ('sat','Satellite'),
            ('sol','solitaire'),
            ('bead','Beaded'),
            ('wov','Woven'),
        ))
    ]
    metal_type = [
        ('Gold',(
           ('fill','Filled'),
           ('verm','Vermeil'),
           ('solid','Solid'),
        )),
        ('Rose Gold',(
           ('fill','Filled'),
           ('verm','Vermeil'),
           ('solid','Solid'),
        )),
        ('White Gold',(
           ('fill','Filled'),
           ('verm','Vermeil'),
           ('solid','Solid'),
        )),
        ('Sterling silver',(
           ('sil','Silver')
        )),
        ('Copper',(
           ('reg','Regular'),
           ('ant','Antique'),
        )),
        ('Brass',(
           ('reg','Regular'),
           ('ant','Antique'),
        )),
        ('Gunmetal',(
           ('gunmetal','Gunmetal'),
        )),
        ('Titanium',(
           ('reg','Regular'),
           ('ano','Anodized')
        )),
        ('Other',(
           ('ela','Elastic'),
           ('thr','Thread'),
        )),
    ]
    stone = models.CharField(max_length=200)
    theme = [
        ('flo','Floral'),
        ('nat','Nature'),
        ('cel','Celestial'),
        ('ast','Astrology'),
        ('bea','Beachy'),
        ('ani','Animals'),
        ('geo','Geometric'),
        ('wor','Words'),
        ('wes','Western'),
        ('cit','City'),
        ('myt','Mythology'),
        ('lan','Landmarks'),
        ('mus','Music'),
        ('foo','Food'),
        ('na','n/a')
    ]
    era = [('trad','Traditional'),('time','Timeless'),('mod','Modern'),('tren','Trendy')]
    thought = [('det','Detailed'),('min','Minimalistic')]
    shape = [('ang','Angular'),('roun','Rounded')]
    style = [('bol','Bold'),('sub','Subtle')]
    cut = [('na','N/A'),('round','Round'),('em','Emerald'),('bril','Brilliant'),('bag','Baguette'),('cus','Cushion'),('mar','Marquise'),('prin','Princess'),('oval','Oval'),('pear','Pear'),('tril','Trillion'),('heart','Heart'),('roy','Royal')]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
