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


import pycbr
from typing import List


from smartclide_dle import config


class GherkinSuggest:

    def predict(self, bpmn:str) -> List[str]:

        # generate recommenation
        cbr = pycbr.CBR([],"ghrkn_recommendator",config.MONGO_IP)
        gherkin_list = cbr.recommend(bpmn)

        # format
        gherkin_list = [{'gherkin': g[0], 'sim': s} for g, s in zip(gherkin_list['gherkins'], gherkin_list['sims'])]
        gherkin_list.sort(key=lambda x: x['sim'], reverse=True)
        gherkin_list = list(set([x['gherkin'] for x in gherkin_list]))

        return gherkin_list
