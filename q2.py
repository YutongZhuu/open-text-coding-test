from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
# Open the webpage
URL = "https://www.microfocus.com/en-us/products?trial=true"
driver.get(URL)

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "products-grid"))
    )

    html = driver.page_source

finally:
    driver.quit()

soup = BeautifulSoup(html, 'html.parser')

product_grid = soup.find('div', class_='products-grid')
grids = soup.find_all(
    'div', class_='uk-card uk-card-hover uk-card-default uk-overflow-hidden uk-margin-large-bottom uk-position-relative')

res = []

for grid in grids:
    product_name = grid.find('div', class_='title').text.strip()
    starting_letter = product_name[0].upper()

    # Assume all cards must have this field
    links = grid.find(
        'div', class_='cta-buttons uk-flex uk-flex-middle').find_all('a')
    demo_url = ""
    free_trial_url = ""
    for button in links:
        if button.text == "Get free trial":  # Assume there are only two types of texts
            free_trial_url = button.get("href")
        else:
            demo_url = button.get("href")

    footer = grid.find('div', class_="footer")
    community_url = ""
    support_url = ""

    if footer:
        links = [link.find('a') for link in footer.find_all('a')]
        for link in links:
            if not link:
                continue

            text = link.text
            if text == 'Community':
                community_url = link.get("href")
            elif text == 'Support':
                support_url = link.get("href")

    res.append({
        'name': product_name,
        'start_letter': starting_letter,
        'demo_url': demo_url,
        'free_trial_url': free_trial_url,
        'community_url': community_url,
        'support_url': support_url
    })

res = json.dumps(res, indent=4)
print(res)

"""result
[
    {
        "name": "Adoption Readiness Tool",
        "start_letter": "A",
        "demo_url": "",
        "free_trial_url": "mailto:ART-Demo@microfocus.com",
        "community_url": "https://community.microfocus.com/welcome_to_the_community/adoption-readiness-tool/",
        "support_url": "/en-us/support/Adoption%20Readiness%20Tool%20(ART)"
    },
    {
        "name": "ALM / Quality Center",
        "start_letter": "A",
        "demo_url": "/en-us/products/alm-quality-center/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ALM Octane",
        "start_letter": "A",
        "demo_url": "/en-us/products/alm-octane/request-demo",
        "free_trial_url": "/en-us/products/alm-octane/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ArcSight Intelligence",
        "start_letter": "A",
        "demo_url": "/en-us/products/arcsight-intelligence/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ArcSight Intelligence for CrowdStrike",
        "start_letter": "A",
        "demo_url": "/en-us/products/arcsight-intelligence-for-crowdstrike/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ArcSight Recon",
        "start_letter": "A",
        "demo_url": "",
        "free_trial_url": "/en-us/products/arcsight-recon/free-trial",
        "community_url": "https://community.microfocus.com/cyberres/arcsight/",
        "support_url": "/en-us/support/ArcSight%20Recon"
    },
    {
        "name": "Asset Management X",
        "start_letter": "A",
        "demo_url": "/en-us/products/asset-management-software/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Cloud Optimizer",
        "start_letter": "C",
        "demo_url": "/en-us/products/cloud-optimizer/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Content Manager Cloud",
        "start_letter": "C",
        "demo_url": "/en-us/products/enterprise-content-management-saas/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Data Protector",
        "start_letter": "D",
        "demo_url": "/en-us/products/data-protector-backup-recovery-software/request-demo",
        "free_trial_url": "/en-us/products/data-protector-backup-recovery-software/free-trial",
        "community_url": "https://community.microfocus.com/img/bandr/",
        "support_url": "/en-us/support/Data%20Protector"
    },
    {
        "name": "Data Protector for Cloud Workloads",
        "start_letter": "D",
        "demo_url": "",
        "free_trial_url": "/en-us/products/data-protector-for-cloud-workloads/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Dimensions RM",
        "start_letter": "D",
        "demo_url": "",
        "free_trial_url": "https://www.microfocus.com/products/dimensions-rm/trial/",
        "community_url": "https://community.microfocus.com/adtd/dimensionsrm/",
        "support_url": "/en-us/support/Dimensions%20RM"
    },
    {
        "name": "Enterprise Suite",
        "start_letter": "E",
        "demo_url": "",
        "free_trial_url": "/en-us/products/enterprise-suite/request-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Filr",
        "start_letter": "F",
        "demo_url": "/en-us/products/filr/request-demo",
        "free_trial_url": "",
        "community_url": "https://community.microfocus.com/collaboration/filr/",
        "support_url": "/en-us/support/Filr"
    },
    {
        "name": "Fortify on Demand",
        "start_letter": "F",
        "demo_url": "/en-us/products/application-security-testing/request-demo",
        "free_trial_url": "/en-us/products/application-security-testing/free-trial",
        "community_url": "https://community.microfocus.com/cyberres/fortify/",
        "support_url": "/en-us/support/Fortify%20on%20Demand"
    },
    {
        "name": "Fortify WebInspect",
        "start_letter": "F",
        "demo_url": "/en-us/products/webinspect-dynamic-analysis-dast/request-demo",
        "free_trial_url": "",
        "community_url": "https://community.microfocus.com/cyberres/fortify/",
        "support_url": "/en-us/support/Fortify%20WebInspect"
    },
    {
        "name": "HCMX FinOps Express",
        "start_letter": "H",
        "demo_url": "/en-us/products/finops-express/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Hybrid Cloud Management X",
        "start_letter": "H",
        "demo_url": "/en-us/products/hybrid-cloud-management-x/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "IDOL",
        "start_letter": "I",
        "demo_url": "/en-us/products/information-data-analytics-idol/request-demo",
        "free_trial_url": "",
        "community_url": "https://community.microfocus.com/t5/IDOL/ct-p/IDOL",
        "support_url": "/en-us/support/IDOL"
    },
    {
        "name": "Law Enforcement Media Analysis",
        "start_letter": "L",
        "demo_url": "/en-us/products/law-enforcement-media-analysis/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "LoadRunner Cloud",
        "start_letter": "L",
        "demo_url": "",
        "free_trial_url": "/en-us/products/loadrunner-cloud/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "LoadRunner Enterprise",
        "start_letter": "L",
        "demo_url": "/en-us/products/loadrunner-enterprise/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "LoadRunner Professional",
        "start_letter": "L",
        "demo_url": "",
        "free_trial_url": "/en-us/products/loadrunner-professional/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "NetIQ Advanced Authentication",
        "start_letter": "N",
        "demo_url": "",
        "free_trial_url": "https://www.netiq.com/products/advanced-authentication/download/",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "NetIQ Data Access Governance (DAG)",
        "start_letter": "N",
        "demo_url": "/en-us/products/data-access-governance/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Network Automation",
        "start_letter": "N",
        "demo_url": "/en-us/products/network-automation/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Network Node Manager i",
        "start_letter": "N",
        "demo_url": "/en-us/products/network-node-manager-i-network-management-software/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Network Operations Management Suite",
        "start_letter": "N",
        "demo_url": "/en-us/products/network-operations-management-suite/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Open Source Select Enterprise",
        "start_letter": "O",
        "demo_url": "/en-us/products/open-source-select-enterprise/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "OpenText Analytics Database Enterprise Edition",
        "start_letter": "O",
        "demo_url": "",
        "free_trial_url": "/en-us/products/analytics-database/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Operations Bridge",
        "start_letter": "O",
        "demo_url": "/en-us/products/operations-bridge/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Operations Bridge Integration Hub",
        "start_letter": "O",
        "demo_url": "",
        "free_trial_url": "/en-us/products/operations-bridge-integration-hub/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Operations Bridge Integration Hub for Partners",
        "start_letter": "O",
        "demo_url": "",
        "free_trial_url": "/en-us/products/operations-bridge-integration-hub1-instance/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Operations Bridge Manager",
        "start_letter": "O",
        "demo_url": "/en-us/products/operations-bridge-manager/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Operations Orchestration with RPA",
        "start_letter": "O",
        "demo_url": "/en-us/products/operations-orchestration-it-process-automation/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Retain Unified Archiving",
        "start_letter": "R",
        "demo_url": "/en-us/products/retain-unified-archiving/request-demo",
        "free_trial_url": "",
        "community_url": "https://community.microfocus.com/t5/Retain/ct-p/Retain",
        "support_url": "/en-us/support/Retain%20Unified%20Archiving"
    },
    {
        "name": "Server Automation",
        "start_letter": "S",
        "demo_url": "/en-us/products/server-automation-software/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Service Management Automation X (SMAX)",
        "start_letter": "S",
        "demo_url": "/en-us/products/service-management-automation-suite/request-demo",
        "free_trial_url": "/en-us/products/service-management-automation-suite/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "SiteScope",
        "start_letter": "S",
        "demo_url": "/en-us/products/sitescope-application-monitoring/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "UFT Developer",
        "start_letter": "U",
        "demo_url": "/en-us/products/uft-developer/request-demo",
        "free_trial_url": "/en-us/products/uft-developer/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "UFT Digital Lab",
        "start_letter": "U",
        "demo_url": "/en-us/products/uft-digital-lab/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "UFT Mobile",
        "start_letter": "U",
        "demo_url": "/en-us/products/uft-mobile/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "UFT One",
        "start_letter": "U",
        "demo_url": "/en-us/products/uft-one/request-demo",
        "free_trial_url": "/en-us/products/uft-one/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Universal Discovery and Universal CMDB",
        "start_letter": "U",
        "demo_url": "/en-us/products/configuration-management-system-database/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Unstructured Data Analytics OEM SDK \u2013 Powered by IDOL",
        "start_letter": "U",
        "demo_url": "/en-us/products/unstructured-data-analytics-oem-sdk/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ValueEdge\u2122 Platform",
        "start_letter": "V",
        "demo_url": "",
        "free_trial_url": "/en-us/products/valueedge/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "VM Explorer",
        "start_letter": "V",
        "demo_url": "",
        "free_trial_url": "/en-us/products/vm-server-backup/request-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Voltage Fusion",
        "start_letter": "V",
        "demo_url": "/en-us/products/voltage-file-analysis-suite/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Voltage Fusion",
        "start_letter": "V",
        "demo_url": "/en-us/products/voltage-fusion/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Voltage SecureData Integrations for Snowflake",
        "start_letter": "V",
        "demo_url": "/en-us/products/voltage-securedata-for-snowflake/request-demo",
        "free_trial_url": "",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "Voltage SecureMail",
        "start_letter": "V",
        "demo_url": "",
        "free_trial_url": "https://www.microfocus.com/products/cloud-email-encryption/free-trial",
        "community_url": "https://community.microfocus.com/t5/Voltage/ct-p/Voltage",
        "support_url": "/en-us/support/Voltage%20SecureMail"
    },
    {
        "name": "Voltage SecureMail Cloud",
        "start_letter": "V",
        "demo_url": "",
        "free_trial_url": "https://www.microfocus.com/en-us/products/cloud-email-encryption/free-trial",
        "community_url": "",
        "support_url": ""
    },
    {
        "name": "ZENworks Suite",
        "start_letter": "Z",
        "demo_url": "",
        "free_trial_url": "https://www.microfocus.com/products/zenworks/trial/",
        "community_url": "",
        "support_url": ""
    }
]
"""
