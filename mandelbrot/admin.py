from django.contrib import admin
from mandelbrot.models import (
    Expert,
    Role,
    Step,
    GithubTeam,
    SlackChannel,
    OnboardingStep,
    Office,
    ContactDetail,
    Project,
    ProjectMember,
)

admin.site.register(Role)
admin.site.register(Step)

admin.site.register(GithubTeam)
admin.site.register(SlackChannel)

admin.site.register(OnboardingStep)
admin.site.register(Office)
admin.site.register(ContactDetail)

admin.site.register(Project)
admin.site.register(ProjectMember)


class OnboardingStepInline(admin.TabularInline):
    model = OnboardingStep


class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMember


class ContactDetailInline(admin.TabularInline):
    model = ContactDetail


class ExpertAdmin(admin.ModelAdmin):
    model = Expert
    inlines = [ProjectMembershipInline, ContactDetailInline, OnboardingStepInline]


admin.site.register(Expert, ExpertAdmin)
