from selenium.webdriver.common.by import By


class BaseActionsLocators:
    PROFILE_BUTTON = (By.XPATH, '//div[@class="right-module-rightButton-39YRvc right-module-mail-25NVA9"]')
    LOGOUT_BUTTON = (By.XPATH, '//div[@class="right-module-rightWrap-3lL6mf"]//ul//li[2]')


class LoginPageLocators:
    MAIN_LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    SUB_LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    INCORRECT_EMAIL_OR_TEL_NUMBER__ELEMENT = (
    By.XPATH, '//div[@class="notify-module-error-drhIFC notify-module-notifyBlock-G7o6Wi"]')
    INVALID_LOGIN_OR_PASSWORD_ELEMENT = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class CampaignsListPageLocators:
    PROFILE_ELEMENT = (By.XPATH, '//div[@class="right-module-rightButton-39YRvc right-module-mail-25NVA9"]')

    FIRST_COMPANY_BUTTON = (By.XPATH, '//a[@href="/campaign/new" and contains(text(), "создайте")]')
    TRAFFIC_GOAL_BUTTON = (By.XPATH, '//div[@class="column-list-item _traffic"]')
    LINK_FIELD = (By.XPATH, '//input[@class="input__inp js-form-element" and @placeholder="Введите ссылку"]')
    CAMPAIGN_NAME_FIELD = (
    By.XPATH, '//div[@class="input input_campaign-name input_with-close"]//input[@class="input__inp js-form-element"]')
    CLEAR_NAME_FIELD_BUTTON = (By.XPATH, '//div[@class="input__clear js-input-clear"]')
    BUDGET_PER_DAY_FIELD = (By.XPATH, '//input[@data-test="budget-per_day"]')
    BUDGET_TOTAL_FIELD = (By.XPATH, '//input[@data-test="budget-total"]')
    BANNER_BUTTON = (By.XPATH, '//span[@class="banner-format-item__title" and contains(text(), "Баннер")]')
    IMG_DROP_FIELD = (By.XPATH, '//input[@data-gtm-id="load_image_btn_240_400"]')
    SUBMIT_UPLOAD_BUTTON = (By.XPATH, '//input[@class="image-cropper__save js-save"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')
    NEW_CAMPAIGN_BUTTON = (By.XPATH, '//span[@data-translated="Create a campaign"]')

    CHECKBOX_FOR_ALL_CAMPAIGNS = (
    By.XPATH, '//input[@class="flexi-table-nt__header__checkbox js-flexi-table_header_checkbox"]')
    ACTIONS_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Действия")]')
    DELETE_BUTTON = (
    By.XPATH, '//span[@class="drop-down-item-view__name js-item-name" and contains(text(), "Удалить")]')

    CAMPAIGN_NAME_ELEM = (By.XPATH, '//a[@class="campaigns-tbl-cell__campaign-name"]')

    SEGMENTS_BUTTON = (By.XPATH, '//a[@class="center-module-button-cQDNvq center-module-segments-3y1hDo"]')


class SegmentsPageLocators:
    NEW_SEGMENT_BUTTON = (By.XPATH, '//button[@class="button button_submit"]')
    FIRST_SEGMENT_BUTTON = (By.XPATH, '//a[@href="/segments/segments_list/new"]')
    ADD_AUDIENCE_SEGMENTS_BUTTON = (
    By.XPATH, '//div[@class="create-segment-form__block create-segment-form__block_add js-add-segments-button"]')
    CHECKBOX1_1 = (By.XPATH,
                   '//div[@class="adding-segments-source__header  adding-segments-source__header_with-icon js-source-header-wrap"]')
    CHECKBOX1_2 = (
    By.XPATH, '//div[@class="payer-settings-view__settings-name-wrap"]//span[@data-translated="Paid on the platform"]')
    CHECKBOX2_1 = (By.XPATH, '//input[@class="adding-segments-source__checkbox js-main-source-checkbox"]')
    SUBMIT_CONFIGURE_SEGMENT_BUTTON = (By.XPATH,
                                       '//button[@data-class-name="Submit"]//div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME_FIELD = (
    By.XPATH, '//div[@class="input input_create-segment-form"]//input[@class="input__inp js-form-element"]')
    SUBMIT_CREATE_SEGMENT_BUTTON = (
    By.XPATH, '//div[@class="create-segment-form__btn-wrap js-create-segment-button-wrap"]//div[@class="button__text"]')

    SEGMENT_NAME_ELEM = (By.XPATH, '//a[@class="adv-camp-cell adv-camp-cell_name"]')

    DELETE_SEGMENT_BUTTON = (By.XPATH, '//span[@class="icon-cross"]')
    CONFIRM_DELETE_SEGMENT_BUTTON = (By.XPATH, '//button[@class="button button_confirm-remove button_general"]')
