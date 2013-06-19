# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scene'
        db.create_table(u'scene_scene', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('music', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('soundfx', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'scene', ['Scene'])

        # Adding model 'Layer'
        db.create_table(u'scene_layer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scene.Scene'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('index', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('grid', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('opacity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=100)),
            ('parallax_axis', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('subtitle_color', self.gf('django.db.models.fields.CharField')(default='#ffffff', max_length=10)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cursor_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cursor_hover', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('float_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('float_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('float_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('filter_scale', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('filter_color', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('filter_speed', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('hit_h', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('hit_w', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('hit_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('hit_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('img_h', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('img_w', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('img_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('img_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('map_orientation', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('map_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('map_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('editor_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'scene', ['Layer'])

        # Adding model 'Grid'
        db.create_table(u'scene_grid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scene.Scene'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'scene', ['Grid'])

        # Adding model 'Matrix'
        db.create_table(u'scene_matrix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scene.Scene'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('axis', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('a_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('a_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('a_value', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('b_x', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('b_y', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('b_value', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'scene', ['Matrix'])


    def backwards(self, orm):
        # Deleting model 'Scene'
        db.delete_table(u'scene_scene')

        # Deleting model 'Layer'
        db.delete_table(u'scene_layer')

        # Deleting model 'Grid'
        db.delete_table(u'scene_grid')

        # Deleting model 'Matrix'
        db.delete_table(u'scene_matrix')


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