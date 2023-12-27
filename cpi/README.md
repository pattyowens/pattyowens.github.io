# Personal CPI Calculator
Author: Patrick Owens <br>
Email: powens457@gmail.com


# Research + Resources
## Bureau of Labor Statistics
### Text Files
- https://download.bls.gov/pub/time.series/cu/
    - The main hub that hosts all of the downloadable text files
- https://download.bls.gov/pub/time.series/cu/cu.txt
    - Overview of the CPI: All Urban Consumers dataset
    - Survey Definition
    - FTP Files listed in the survery directory
    - Time series, series file, data file, & mapping file definitions & relationships
    - Series file format and field definitions
    - Data file format and field definitions
    - Mapping file formats and field definitions
    - Data Element Dictionary
- https://download.bls.gov/pub/time.series/cu/cu.series
    - All of the tracked series, broken up by: 
        - series_id: unique identifier for a given series. Details in cu.series
        - area_code: Area codes specific to that series. Details in cu.area
        - item_code: Unique code for each item bucket. Details in cu.item
        - seasonal: S - Seasonally Adjusted or U - Not Seasonally Adjusted. Details in cu.seasonal
        - periodicity_code: S - Semi-Annual or R - Monthly. Details in cu.periodicity 
        - base_code: S - Current or A - Alternate. Details in cu.base 
        - base_period: The initial timeframe that the series is based on
        - series_title: Human readabale series description
        - footnote_codes: N/A
        - begin_year: The year the series began 
        - begin_period: The month the series began. Details in cu.period
        - end_year: The year the series ended
        - end_period:  The month that the series ended. Details in cu.period

### APIs


### Terms of Service
#### Scope
All of the content, documentation, code and related materials made available to users through BLS.gov is subject to these terms. Access to or use of BLS.gov services or its content constitutes acceptance to this Agreement.

#### Secondary Use
Data accessed through BLS.gov do not, and should not, include controls over its end use. However, as the data owners or authoritative sources, the Departments and Agencies providing the data retain version control. Once the data have been downloaded from BLS.gov, the U.S. Bureau of Labor Statistics cannot vouch for the quality and timeliness of any analyses conducted with retrieved data.

#### Citing Data
Users of the public API should cite the date that data were accessed or retrieved using the API. Users must clearly state that “BLS.gov cannot vouch for the data or analyses derived from these data after the data have been retrieved from BLS.gov.” The BLS.gov logo may not be used by persons who are not BLS employees or on products (including web pages) that are not BLS-sponsored.

#### Public Participation
In support of the Transparency and Open Government Initiative, recommendations from individuals, groups, and organizations regarding the presentation of data, data types, and metadata will contribute to the evolution of BLS.gov’s public APIs.

#### Modification or False Representation of Content
Users may not modify or falsely represent content accessed through BLS.gov and still cite the source as BLS.gov.

#### Right to Limit
Use of the APIs may be subject to certain limitations on access, calls, or use as set forth within this Agreement or otherwise provided by BLS. If BLS reasonably believes that a user has attempted to exceed or circumvent these limits, that user's access to the API may be permanently or temporarily blocked.

BLS may monitor your use of its services to improve the service or to ensure compliance with this Agreement.

#### Service Termination
If a user wishes to terminate this Agreement, he/she may do so by refraining from further use of the services. BLS reserves the right (though not the obligation) to (1) refuse to provide the services to a user, if it is BLS’s opinion that use violates any BLS policy, or (2) terminate or deny a user’s access to and use of all or part of the services at any time for any other reason in its sole discretion. Any hosted applications may also be shut down or removed. All provisions of this Agreement, which by their nature should survive termination, shall survive termination including, without limitation, warranty disclaimers, indemnity, and limitations of liability.

#### Changes
BLS reserves the right, at its sole discretion, to modify or replace this Agreement, in whole or in part. Continued use of or access to the BLS.gov services following posting of any changes to this Agreement constitutes acceptance of those modified terms. BLS may, in the future, offer new services and/or features. Such new features and/or services shall be subject to the terms and conditions of this Agreement.

#### Disclaimer of Warranties
BLS.gov services are provided “as is” and on an “as-available” basis. BLS hereby disclaims all warranties of any kind, express or implied, including without limitation the warranties of merchantability, fitness for a particular purpose, and non-infringement. BLS makes no warranty that the services will be error free or that access thereto will be continuous or uninterrupted.

#### Limitations on Liability
In no event will BLS be liable with to respect to any subject matter of this Agreement under any contract, negligence, strict liability or other legal or equitable theory for: (1) any special, incidental, or consequential damages; (2) the cost of procurement of substitute products or services; or (3) interruption of use or loss or corruption of data.

#### General Representations
The user hereby warrant that (1) his/her use of the services will be in strict accordance with the BLS.gov privacy policy, this Agreement, and all applicable laws and regulations, and (2) his/her use of the services will not infringe or misappropriate the intellectual property rights of any third party.

#### Indemnification
The user agrees to indemnify and hold harmless BLS, its contractors, employees, agents, and the like from and against any and all claims and expenses including attorney’s fees, arising out of your use of the APIs, including but not limited to violation of this Agreement. This Indemnification clause shall not apply to government entities.

#### Miscellaneous
This Agreement constitutes the entire Agreement between BLS and the user concerning the subject matter hereof, and may only be modified by the posting of a revised version on this page by BLS.

#### Disputes
Any disputes arising out of this Agreement and access to or use of the services shall be governed by federal law.

#### No Waiver of Rights
BLS’s failure to exercise or enforce any right or provision of this Agreement shall not constitute waiver of such right or provision.