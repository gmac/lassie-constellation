# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Dialogue.puppet'
        db.delete_column(u'interaction_dialogue', 'puppet')

        # Adding field 'Dialogue.related_target'
        db.add_column(u'interaction_dialogue', 'related_target',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'Dialogue.voice'
        db.alter_column(u'interaction_dialogue', 'voice_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['interaction.Voice']))
        # Adding field 'Voice.subtitle_color'
        db.add_column(u'interaction_voice', 'subtitle_color',
                      self.gf('django.db.models.fields.CharField')(default='#FFFFFF', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Dialogue.puppet'
        db.add_column(u'interaction_dialogue', 'puppet',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Deleting field 'Dialogue.related_target'
        db.delete_column(u'interaction_dialogue', 'related_target')


        # Changing field 'Dialogue.voice'
        db.alter_column(u'interaction_dialogue', 'voice_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interaction.Voice'], null=True))
        # Deleting field 'Voice.subtitle_color'
        db.delete_column(u'interaction_voice', 'subtitle_color')


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
            'related_target': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'sound': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'voice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interaction.Voice']"})
        },
        u'interaction.voice': {
            'Meta': {'object_name': 'Voice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subtitle_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '10'}),
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