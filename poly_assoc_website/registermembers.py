#!/home/boca/.virtualenvs/PolyEnv/bin/python


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import md5, sha

import sys

sys.path.append('/home/boca/.virtualenvs/PolyEnv')
sys.path.append('/home/boca/djsites/PolyAssocWebsite')

from django.core.management import setup_environ

import settings as st
setup_environ(st)

from poly_assoc_website.models import User,  MemberProfile
from django.contrib.auth.models import Group

import datetime as dt


users = User.objects.all()
member_group = Group.objects.get(name='AssociationMembers')



log_file = open('registred_members.txt','wb')

def register_members():
	for user in users:
		if user.is_authenticated():
			u_groups = user.groups.all()
			if member_group not in u_groups:
				user.groups.add(member_group)
			for perm in member_group.permissions.all():
				if user not in perm.user_set.all():
					perm.user_set.add(user)
					log_text = 'User (%s, %s)  registred at the base at %s' % (user.username,user.email,dt.datetime.now())
					log_file.write(log_text)
			#print log_text

register_members()
log_file.close()

