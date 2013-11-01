#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-08-21.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import bpy
import sys
import os


def delete_all_meshes():
	bpy.ops.object.select_all()
	# gather list of items of interest.
	candidate_list = [item.name for item in bpy.data.objects if item.type == "MESH"]
	# select them only.
	for object_name in candidate_list:
	  bpy.data.objects[object_name].select = True
	# remove all selected.
	bpy.ops.object.delete()
	# remove the meshes, they have no users anymore.
	for item in bpy.data.meshes:
	  bpy.data.meshes.remove(item)




	
	

def main():
	delete_all_meshes()
	

if __name__ == '__main__':
	main()

