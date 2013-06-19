# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voice'
        db.create_table(u'interaction_voice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'interaction', ['Voice'])

        # Adding model 'Dialogue'
        db.create_table(u'interaction_dialogue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('puppet', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('tone', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sound', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('voice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interaction.Voice'], null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interaction.Action'])),
        ))
        db.send_create_signal(u'interaction', ['Dialogue'])

        # Adding model 'ActionType'
        db.create_table(u'interaction_actiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_generic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_item', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'interaction', ['ActionType'])

        # Adding model 'Action'
        db.create_table(u'interaction_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('grammar', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('script', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('related_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'], null=True, blank=True)),
            ('action_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interaction.ActionType'])),
        ))
        db.send_create_signal(u'interaction', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Voice'
        db.delete_table(u'interaction_voice')

        # Deleting model 'Dialogue'
        db.delete_table(u'interaction_dialogue')

        # Deleting model 'ActionType'
        db.delete_table(u'interaction_actiontype')

        # Deleting model 'Action'
        db.delete_table(u'interaction_action')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'interaction.action': {
            'Meta': {'object_name': 'Action'},
            'action_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interaction.ActionType']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'grammar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'related_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'interaction.actiontype': {
            'Meta': {'object_name': 'ActionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_generic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_item': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'interaction.dialogue': {
            'Meta': {'ordering': "['index']", 'object_name': 'Dialogue'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interaction.Action']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'puppet': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'sound': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'voice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interaction.Voice']", 'null': 'True', 'blank': 'True'})
        },
        u'interaction.voice': {
            'Meta': {'object_name': 'Voice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['interaction']