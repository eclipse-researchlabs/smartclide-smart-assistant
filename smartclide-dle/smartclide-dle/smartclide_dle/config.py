#!/usr/bin/python3
#*******************************************************************************
# Copyright (C) 2021-2022 AIR Institute
# 
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
# 
# SPDX-License-Identifier: EPL-2.0
#*******************************************************************************


import os

# api config
PORT = os.getenv('DLE_API_PORT', 5001) 
HOST = os.getenv('DLE_API_BIND', '0.0.0.0')
URL_PREFIX = '/smartclide/v1'
DEBUG_MODE = True

# mongodb configuration
MONGO_DB = os.getenv('DLE_MONGODB_DB', 'smartclide-smart-assistant')
MONGO_IP = os.getenv('DLE_MONGODB_HOST', 'localhost') 
MONGO_PORT = os.getenv('DLE_MONGODB_PORT', 27017)
MONGO_USER = os.getenv('DLE_MONGODB_USER', 'user') 
MONGO_PASSWORD = os.getenv('DLE_MONGODB_PASSWORD', 'password') 
MONGO_URI = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_IP}:{MONGO_PORT}/{MONGO_DB}'
