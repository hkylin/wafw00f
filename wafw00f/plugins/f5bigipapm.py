#!/usr/bin/env python


NAME = 'BIG-IP Access Policy Manager (F5 Networks)'


def is_waf(self):
    # the following based on nmap's http-waf-fingerprint.nse
    if self.matchcookie('^LastMRH_Session') and self.matchcookie('^MRHSession'):
        return True
    elif self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')) and self.matchcookie('^MRHSession'):
        return True
    if self.matchheader(('Location', '\/my.policy')) and self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('Location', '\/my\.logout\.php3')) and self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('Location', '.+\/f5\-w\-68747470.+')) and self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.matchcookie('^F5_fullWT') or self.matchcookie('^F5_ST') or self.matchcookie('^F5_HT_shrinked'):
        return True
    elif self.matchcookie('^MRHSequence') or self.matchcookie('^MRHSHint') or self.matchcookie('^LastMRH_Session'):
        return True
    else:
        return False