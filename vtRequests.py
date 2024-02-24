#!/usr/bin/env python3

import json
import subprocess
import sys
import hashPerm
import regex

# Centralize all Virus Total API requests here
class vtAPIRequests:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.ipv4Pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        self.getTemplateFirst = "curl --request GET --url https://www.virustotal.com/api/v3/"
        self.getTemplateSecond = " --header 'x-apikey: " + self.apiKey + "'"

    def run(self, curlRequest):
        ret = subprocess.run(string, capture_output=True, shell=True)
        return json.loads(ret.stdout.decode())['data']['attributes']['last_analysis_stats']
    
    def extract(self, extra):
        if re.search(self.ipv4Pattern, extra):
            ipCurl = self.getTemplate + "ip_addresses/" + extra + self.getTemplateSecond
            return self.trustIP(self.self.get(ipCurl))
        else:
            hashCurl = self.getTemplate + "files/" + extra + self.getTemplateSecond
            return self.trustFileHash(self.get(hashCurl))

    def trustFileHash(self):
        if self.data == "No data" or self.data['harmless'] >= self.data['malicious'] and self.data['malicious'] < 3:
            return True
        else:
            return False

    def trustIP(self):
        try:
            score = self.data['harmless']/(self.data['malicious']*5)
            if score > 3:
                return True
            else:
                return False
        except:
            # Divide by zero
            if self.data['harmless'] >= 1:
                return True
            else:
                return False

    def file_hasher(self, _file):
        try:
            with open(_file, 'rb') as f:
                sha = hashlib.sha256()
                buf = f.read()
                sha.update(buf)
                self.files[_file] = sha.hexdigest()
        except:
            print(_file + " did not convert!")

    def getFileRep(self, _file):
        return self.extract(self.file_hasher(_file))

    def getIPRep(self, ip):
        return self.extract(ip)
