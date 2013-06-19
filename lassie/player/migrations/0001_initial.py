# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InventoryCollection'
        db.create_table(u'player_inventorycollection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'player', ['InventoryCollection'])

        # Adding M2M table for field items on 'InventoryCollection'
        m2m_table_name = db.shorten_name(u'player_inventorycollection_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inventorycollection', models.ForeignKey(orm[u'player.inventorycollection'], null=False)),
            ('item', models.ForeignKey(orm[u'inventory.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inventorycollection_id', 'item_id'])

        # Adding model 'DefaultResponse'
        db.create_table(u'player_defaultresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'player', ['DefaultResponse'])

        # Adding model 'Avatar'
        db.create_table(u'player_avatar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('inventory_collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player.InventoryCollection'])),
            ('default_response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player.DefaultResponse'])),
        ))
        db.send_create_signal(u'player', ['Avatar'])


    def backwards(self, orm):
        # Deleting model 'InventoryCollection'
        db.delete_table(u'player_inventorycollection')

        # Removing M2M table for field items on 'InventoryCollection'
        db.delete_table(db.shorten_name(u'player_inventorycollection_items'))

        # Deleting model 'DefaultResponse'
        db.delete_table(u'player_defaultresponse')

        # Deleting model 'Avatar'
        db.delete_table(u'player_avatar')


    models = {
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'player.avatar': {
            'Meta': {'object_name': 'Avatar'},
            'default_response': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['player.DefaultResponse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory_collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['player.InventoryCollection']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'player.defaultresponse': {
            'Meta': {'object_name': 'DefaultResponse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'player.inventorycollection': {
            'Meta': {'object_name': 'InventoryCollection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['player']