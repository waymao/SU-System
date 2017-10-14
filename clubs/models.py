from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    hash = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    publish_date = models.DateTimeField('date published')
    description = models.TextField(max_length=2000)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MemberInfo(models.Model):
    # 所有的团员注册状态
    APPROVED = 'AP'
    WAITLIST = 'WL'
    NOT_APPROVED = 'NA'
    NOT_VIEWED = 'NV'

    APPROVAL_STATUS_CHOICES = (
        (APPROVED, '正式社员'),
        (WAITLIST, '等候列表'),
        (NOT_APPROVED, '非社员'),
        (NOT_VIEWED, '未审核')
    )

    # 团员类型
    PRESIDENT = 'PR'
    VICE_PRESIDENT = 'VP'
    FINANCIAL_MANAGER = 'FM'
    CORE_STUFF = 'CS'
    ORDINARY_MEMBER = 'MB'

    MEMBER_TYPE_CHOICES = (
        (PRESIDENT, '社长'),
        (VICE_PRESIDENT, '副社长'),
        (FINANCIAL_MANAGER, '财务'),
        (CORE_STUFF, '社团核心成员'),
        (ORDINARY_MEMBER, '社团')
    )

    club_ref = models.ForeignKey(Club, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    ApprovalStatus = models.CharField(
        max_length=2,
        choices=APPROVAL_STATUS_CHOICES,
        default=NOT_VIEWED
    )
    # Approved, not approved, waitlist, not_viewed

    Member_type = models.CharField(
        max_length=2,
        choices=MEMBER_TYPE_CHOICES,
        default=ORDINARY_MEMBER
    )

    # Participant, judge, audience, staff, admin

    def __str__(self):
        return "(" + self.ApprovalStatus + ")" + str(self.member) + " is the member of " + str(
            self.club_ref) + " as a " + self.Member_type

# Create your models here.
