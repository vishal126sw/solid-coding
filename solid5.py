# Dependency Inversion Principle

from enum import Enum
from abc import abstractmethod

class Clubs(Enum):
    Swim = 1
    Cycle = 2
    Run = 3

class Student():
    def __init__(self,name):
        self.name = name

class ClubMembershipsLookup():
    @abstractmethod
    def find_all_students_from_club(self,club):
        pass

class ClubMemberships(ClubMembershipsLookup):
    def __init__(self):
        self.club_memberships=[]
    def add_club_membership(self,student,club):
        self.club_memberships.append((student,club))
    def find_all_students_from_club(self,club):
        for members in self.club_memberships:
            if(members[1]==club):
                yield members[0].name
    

class InspectMemberships():
    def __init__(self,club_membership_lookup):
        for student in club_membership_lookup.find_all_students_from_club(Clubs.Swim):
            print(f'{student} is in the SWIM Club.')
        for student in club_membership_lookup.find_all_students_from_club(Clubs.Run):
            print(f'{student} is in the RUN Club.')
        for student in club_membership_lookup.find_all_students_from_club(Clubs.Cycle):
            print(f'{student} is in the CYCLE Club.')

    

student_one = Student('Johnny')
student_two = Student('Bobby')
student_three = Student('Amy')

club_memberships = ClubMemberships()
club_memberships.add_club_membership(student_one, Clubs.Swim)
club_memberships.add_club_membership(student_two, Clubs.Run)
club_memberships.add_club_membership(student_three, Clubs.Cycle)

InspectMemberships(club_memberships)