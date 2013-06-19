# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Layer.group'
        db.add_column(u'scene_layer', 'group',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Layer.hit_enabled'
        db.add_column(u'scene_layer', 'hit_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Layer.group'
        db.delete_column(u'scene_layer', 'group')

        # Deleting field 'Layer.hit_enabled'
        db.delete_column(u'scene_layer', 'hit_enabled')


    models = {
        u'scene.grid': {
            'Meta': {'object_name': 'Grid'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scene.Scene']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'})
        },
        u'scene.layer': {
            'Meta': {'object_name': 'Layer'},
            'cursor_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cursor_hover': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'editor_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'filter_color': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'filter_scale': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'filter_speed': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'float_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'float_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'float_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'grid': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'group': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'hit_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hit_h': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'hit_w': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'hit_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'hit_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'img_h': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'img_w': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'img_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'img_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'index': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'map_orientation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'map_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'map_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'opacity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'parallax_axis': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scene.Scene']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'subtitle_color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'scene.matrix': {
            'Meta': {'object_name': 'Matrix'},
            'a_value': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'a_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'a_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'axis': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'b_value': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'b_x': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'b_y': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scene.Scene']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'scene.scene': {
            'Meta': {'object_name': 'Scene'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'music': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'soundfx': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['scene']