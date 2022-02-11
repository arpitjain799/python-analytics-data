# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CheckCompatibility
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-analytics-data


# [START analyticsdata_generated_data_v1beta_BetaAnalyticsData_CheckCompatibility_async]
from google.analytics import data_v1beta


async def sample_check_compatibility():
    # Create a client
    client = data_v1beta.BetaAnalyticsDataAsyncClient()

    # Initialize request argument(s)
    request = data_v1beta.CheckCompatibilityRequest(
    )

    # Make the request
    response = await client.check_compatibility(request=request)

    # Handle the response
    print(response)

# [END analyticsdata_generated_data_v1beta_BetaAnalyticsData_CheckCompatibility_async]