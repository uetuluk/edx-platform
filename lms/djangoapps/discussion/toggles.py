"""
Discussions feature toggles
"""
from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag

WAFFLE_FLAG_NAMESPACE = "discussions"

# .. toggle_name: discussions.enable_discussions_mfe
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to use the new MFE experience for discussions in the course tab and in-context
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2021-11-05
# .. toggle_target_removal_date: 2022-03-05
ENABLE_DISCUSSIONS_MFE = CourseWaffleFlag(f'{WAFFLE_FLAG_NAMESPACE}.enable_discussions_mfe', __name__)

# .. toggle_name: discussions.enable_discussions_mfe_for_everyone
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to use the new MFE experience for discussions in the course tab and in-context
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2021-04-21
# .. toggle_target_removal_date: 2022-03-05
ENABLE_DISCUSSIONS_MFE_FOR_EVERYONE = CourseWaffleFlag(
    f'{WAFFLE_FLAG_NAMESPACE}.enable_discussions_mfe_for_everyone', __name__
)

# .. toggle_name: discussions.enable_new_structure_discussions
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to toggle on the new structure for in context discussions
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2022-02-22
# .. toggle_target_removal_date: 2022-09-22
ENABLE_NEW_STRUCTURE_DISCUSSIONS = CourseWaffleFlag(
    f'{WAFFLE_FLAG_NAMESPACE}.enable_new_structure_discussions', __name__
)

# .. toggle_name: discussions.enable_learners_tab_in_discussions_mfe
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to enable learners tab in the new MFE experience for discussions
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2022-02-21
# .. toggle_target_removal_date: 2022-05-21
# lint-amnesty, pylint: disable=line-too-long
ENABLE_LEARNERS_TAB_IN_DISCUSSIONS_MFE = CourseWaffleFlag(
    f'{WAFFLE_FLAG_NAMESPACE}.enable_learners_tab_in_discussions_mfe', __name__
)

# .. toggle_name: discussions.enable_moderation_reason_codes
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to toggle support for the new edit and post close reason codes
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2022-02-22
# .. toggle_target_removal_date: 2022-09-22
ENABLE_DISCUSSION_MODERATION_REASON_CODES = CourseWaffleFlag(
    f'{WAFFLE_FLAG_NAMESPACE}.enable_moderation_reason_codes', __name__
)

# .. toggle_name: discussions.enable_reported_content_email_notifications
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to toggle email notifications for reported content for moderators
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2022-03-08
# .. toggle_target_removal_date: 2022-12-31
ENABLE_REPORTED_CONTENT_EMAIL_NOTIFICATIONS = CourseWaffleFlag(
    f'{WAFFLE_FLAG_NAMESPACE}.enable_reported_content_email_notifications', __name__
)

# .. toggle_name: discussions.enable_mfe_banner_for_learners
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to enable new MFE banner for learners
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2022-06-08
# .. toggle_target_removal_date: 2022-09-05
ENABLE_DISCUSSIONS_MFE_BANNER = CourseWaffleFlag(f'{WAFFLE_FLAG_NAMESPACE}.enable_mfe_banner_for_learners', __name__)
