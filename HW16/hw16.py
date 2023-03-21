"""XPATH(3steps)"""
# 1
from_header_to_child_and_descendant = '//div[@class="page__header"]/child::div[@class="container"]/descendant::nav[@class="header"]'
# 2
from_right_side_bar_to_descendant_and_following = '//div[@class="columns__wrap columns__wrap--right"]/descendant::*[@class="interface-hints-icon"]/following::*[@class="ng-star-inserted"]'
# 3
from_header_to_ancestors = '//ul[@class="breadcrumbs ng-star-inserted"]/ancestor::div[@class="header__wrapper"]/ancestor::div[@class="header__container"]'

"""XPATH(1step)"""
# 4
header = '//nav[@class="header"]'
"""css"""
header = 'nav.header'
# 5
left_side_bar = '//aside[@class="page__aside page__aside--locked ng-star-inserted"]'
"""css"""
left_side_bar = 'div aside'
# 6
right_side_bar = '//div[@class="columns__wrap columns__wrap--right"]'
"""css"""
right_side_bar = 'div[class*="columns__wrap columns__wrap--right"]'
# 7
homeworks_footer = '//div[@class="homework__info-footer"]'
"""css"""
homeworks_footer = 'div.homework__info-footer'
# 8
homeworks_and_points = '//th[@class="widget-table__header-description"]'
"""css"""
homeworks_and_points = 'th.widget-table__header-description'

"""""XPATH(2 steps)"""
# 9
from_header_to_following = '//div[@class="container"]/following::div[@class="page__body"]'
"""css"""
from_header_to_following = 'div.page__body'
# 10
from_right_side_bar_to_ancestor = '//div[@class="columns__wrap columns__wrap--right"]/ancestor::div[@class="page"]'
"""css"""
from_right_side_bar_to_ancestor = 'app-page div.page'
# 11
from_homework_header_to_parent = '//div[@class="homework__info-header"]/parent::div[@class="homework__info"]'
"""css"""
from_homework_header_to_parent = 'div.homework__info'
# 12
from_user_photo_to_ancestor = '//div[@class="user-photo-message"]/ancestor::ul[@class="header__list"]'
"""css"""
from_user_photo_to_ancestor = 'ul.header__list'
# 13
from_send_homework_button_to_parent = '//button[@class="homework__button hi-button ng-star-inserted"]/parent::div[@class="homework__buttons ng-star-inserted"]'
"""css"""
from_send_homework_button_to_parent = 'div[class*="homework__buttons ng-star-inserted"]'
# 14
from_page_header_to_child = '//div[@class="page__header"]/child::div[@class="container"]'
# 15
from_homework_info_header_to_following = '//span[@class="homework__info-header-title-text"]/following::div[@class="homework__info-header-title-data"]'
# 16
from_deadlines_to_parent = '//span[@class="reference-course__text-description ng-star-inserted"]/parent::div[@class="reference-course__text"]'
# 17
from_basic_methods_to_ancestor = '//span[@class="reference-course__text-description ng-star-inserted"]/ancestor::div[@class="reference-course__text"]'
# 18
from_homework_status_to_following = '//app-grade-badge[@apptooltipposition="below"]/following::div[@class="homework__info-header-terms"]'
# 19
from_back_to_homeworks_to_following = '//span[@class="homework__back-link-text"]/following::div[@class="homework__info"]'
# 20
from_homework_time_to_parent = '//time[@class="group-page__date"]/parent::section[@class="group-page__head ng-star-inserted"]'
# 21
from_homeworks_title_to_parent = '//span[@class="breadcrumbs__item-link-label"]/parent::*[@class="breadcrumbs__item-link"]'
# 22
from_group_title_to_parent = '//h1[@class="group-page__title"]/parent::section[@class="group-page__head ng-star-inserted"]'
# 23
from_discuss_homework_to_ancestor = '//span[@class="button-icon-label"]/ancestor::button[@hi-button="secondary icon"]'
# 24
from_help_link_to_child = '//a[@href="/help"]/child::*[@viewBox="0 0 24 24"]'
# 25
from_calendar_to_following = '//a[@href="/calendar"]/following::li[@class="menu-aside__item ng-tns-c134-13"]'
# 26
from_home_button_to_following = '//li[@class="menu-aside__item ng-tns-c134-13"]/following::button[@class="menu-aside__selection ng-tns-c134-13"]'
# 27
from_discuss_button_to_parent = '//li[@class="header__item ng-star-inserted"]/parent::ul[@class="header__list"]'
# 28
from_header_to_child = 'https://lms.ithillel.ua/groups/6374d610e8c1aa52b9f0929b/homeworks/6413673a406fbb7d651b0825'
# 29
from_homework_link_to_preceding = '//a[@class="homework__info-header-lesson-action"]/preceding::div[@class="homework__info-header-terms"]'
# 30
from_homework_punishment_info_to_child = '//div[@class="homework__info-content-prompt"]/child::div[@class="homework__punishment-info"]'
