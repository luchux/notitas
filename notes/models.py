from django.db import models
from django.forms import ModelForm


#------ Model Tag -------#
# Represents a tag, with a text string.
# Unique text, and a counter attribute to store number of uses of hash.
#------------------------#
class Tag(models.Model):
    tag = models.CharField('tag', max_length=100, unique=True)
    count = models.IntegerField('count', default=0)

    def __unicode__(self):
        return self.tag


#------ Model Note -------#
# Represents a Note, with a text string, creation date and
# a M2M relation to tags (Tag).
#-------------------------#
class Note(models.Model):

    text = models.CharField('text', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    # Redefinition of save(): when a note is saved, we extract the tags,
    # and if the tags doesn't exist it creates it. Incrementing +1 the counter
    # of Tag.
    def save(self, *args, **kwargs):
        super(Note, self).save()
        tags_text = {tag.strip('#') for tag in self.text.split() if tag.startswith('#')}

        tags = Tag.objects.all()
        for tag in tags_text:
            t, created = tags.get_or_create(tag=tag)
            t.count += 1
            t.save()
            self.tags.add(t)

    # __unicode__ method to use as text for represent the node. Used in the admin.
    def __unicode__(self):
        return self.text[:5]


#------ ModelForm NoteForm -------#
# This NoteForm class, represents the form for Note model.
# This django feature allows the generation of the form for
# every attribute in the model.
#---------------------------------#
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text',)
