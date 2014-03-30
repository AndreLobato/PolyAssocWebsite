# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NewsTranslation'
        db.create_table('cmsplugin_advancednews_news_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['cmsplugin_advancednews.News'])),
        ))
        db.send_create_signal('cmsplugin_advancednews', ['NewsTranslation'])

        # Adding unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.create_unique('cmsplugin_advancednews_news_translation', ['language_code', 'master_id'])

        # Adding model 'News'
        db.create_table('cmsplugin_advancednews_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='n_category', null=True, blank=True, to=orm['cmsplugin_advancednews.Category'])),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 12, 20, 3, 19, 12, 359953))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_advancednews', ['News'])

        # Adding model 'CategoryTranslation'
        db.create_table('cmsplugin_advancednews_category_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['cmsplugin_advancednews.Category'])),
        ))
        db.send_create_signal('cmsplugin_advancednews', ['CategoryTranslation'])

        # Adding unique constraint on 'CategoryTranslation', fields ['language_code', 'master']
        db.create_unique('cmsplugin_advancednews_category_translation', ['language_code', 'master_id'])

        # Adding model 'Category'
        db.create_table('cmsplugin_advancednews_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 12, 20, 3, 19, 12, 364270))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_advancednews', ['Category'])

        # Adding model 'LatestAdvancedNewsPlugin'
        db.create_table('cmsplugin_latestadvancednewsplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['cmsplugin_advancednews.Category'], null=True, blank=True)),
            ('limit', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('cmsplugin_advancednews', ['LatestAdvancedNewsPlugin'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CategoryTranslation', fields ['language_code', 'master']
        db.delete_unique('cmsplugin_advancednews_category_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.delete_unique('cmsplugin_advancednews_news_translation', ['language_code', 'master_id'])

        # Deleting model 'NewsTranslation'
        db.delete_table('cmsplugin_advancednews_news_translation')

        # Deleting model 'News'
        db.delete_table('cmsplugin_advancednews_news')

        # Deleting model 'CategoryTranslation'
        db.delete_table('cmsplugin_advancednews_category_translation')

        # Deleting model 'Category'
        db.delete_table('cmsplugin_advancednews_category')

        # Deleting model 'LatestAdvancedNewsPlugin'
        db.delete_table('cmsplugin_latestadvancednewsplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_advancednews.category': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 20, 3, 19, 12, 364270)'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'cmsplugin_advancednews.categorytranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'CategoryTranslation', 'db_table': "'cmsplugin_advancednews_category_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['cmsplugin_advancednews.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'cmsplugin_advancednews.latestadvancednewsplugin': {
            'Meta': {'object_name': 'LatestAdvancedNewsPlugin', 'db_table': "'cmsplugin_latestadvancednewsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['cmsplugin_advancednews.Category']", 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'cmsplugin_advancednews.news': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'News'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'n_category'", 'null': 'True', 'blank': 'True', 'to': "orm['cmsplugin_advancednews.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 20, 3, 19, 12, 359953)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'cmsplugin_advancednews.newstranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'NewsTranslation', 'db_table': "'cmsplugin_advancednews_news_translation'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['cmsplugin_advancednews.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_advancednews']
