# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JaActivePagesSource(models.Model):
    source = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'ja_active_pages_source'


class JaActivePagesValue(models.Model):
    ps_id = models.IntegerField()
    project_management_id = models.IntegerField()
    active_user = models.IntegerField()
    new_session = models.FloatField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'ja_active_pages_value'


class JaAdConfig(models.Model):
    section1_html = models.TextField(blank=True, null=True)
    section1_html_mobile = models.TextField(blank=True, null=True)
    section2_html = models.TextField(blank=True, null=True)
    section3_html = models.TextField(blank=True, null=True)
    section4_html = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_ad_config'


class JaAddOns(models.Model):
    add_on_name = models.CharField(max_length=255)
    unique_name = models.CharField(unique=True, max_length=255)
    version = models.CharField(max_length=255)
    installed_at = models.DateTimeField()
    update_at = models.DateTimeField()
    purchase_code = models.CharField(max_length=100)
    module_folder_name = models.CharField(max_length=255)
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_add_ons'


class JaAdminNotifications(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
    project_management_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_admin_notifications'


class JaAiParameters(models.Model):
    project_management_id = models.PositiveIntegerField()
    lr = models.FloatField(blank=True, null=True)
    decay = models.FloatField(blank=True, null=True)
    epoch = models.IntegerField(blank=True, null=True)
    dropout = models.FloatField(blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    lstm_shape = models.CharField(max_length=50, blank=True, null=True)
    dense_shape = models.CharField(max_length=50, blank=True, null=True)
    optimizer = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_ai_parameters'


class JaAiPredictions(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ecommerce_users = models.FloatField(blank=True, null=True)
    total_revenue = models.FloatField(blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)
    total_transactions = models.IntegerField(blank=True, null=True)
    avg_order_value = models.FloatField(blank=True, null=True)
    total_ads_clicks = models.IntegerField(blank=True, null=True)
    total_ads_cost = models.FloatField(blank=True, null=True)
    ads_cpc_value = models.FloatField(blank=True, null=True)
    mcf_conversion = models.FloatField(blank=True, null=True)
    mcf_conversion_value = models.FloatField(blank=True, null=True)
    mcf_assisted_conversion = models.FloatField(blank=True, null=True)
    mcf_assisted_value = models.FloatField(blank=True, null=True)
    social_facebook_clicks = models.IntegerField(blank=True, null=True)
    social_twitter_clicks = models.IntegerField(blank=True, null=True)
    social_pinterest_clicks = models.IntegerField(blank=True, null=True)
    social_instagram_clicks = models.IntegerField(blank=True, null=True)
    new_visitors = models.IntegerField(blank=True, null=True)
    returning_visitors = models.IntegerField(blank=True, null=True)
    total_users = models.IntegerField(blank=True, null=True)
    total_pageviews = models.IntegerField(blank=True, null=True)
    bounce_rate = models.FloatField(blank=True, null=True)
    total_sessions = models.IntegerField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True)
    session_by_desktop = models.FloatField(blank=True, null=True)
    session_by_tablet = models.FloatField(blank=True, null=True)
    session_by_mobile = models.FloatField(blank=True, null=True)
    total_mobile_users = models.IntegerField(blank=True, null=True)
    total_desktop_users = models.IntegerField(blank=True, null=True)
    total_tablet_users = models.IntegerField(blank=True, null=True)
    total_paid_pageviews = models.IntegerField(blank=True, null=True)
    total_paid_users = models.IntegerField(blank=True, null=True)
    total_referral_pageviews = models.IntegerField(blank=True, null=True)
    total_referral_users = models.IntegerField(blank=True, null=True)
    total_organic_pageviews = models.IntegerField(blank=True, null=True)
    total_organic_users = models.IntegerField(blank=True, null=True)
    total_direct_pageviews = models.IntegerField(blank=True, null=True)
    total_direct_users = models.IntegerField(blank=True, null=True)
    total_email_pageviews = models.IntegerField(blank=True, null=True)
    total_email_users = models.IntegerField(blank=True, null=True)
    fb_clicks = models.IntegerField(blank=True, null=True)
    fb_cpc = models.FloatField(blank=True, null=True)
    fb_impressions = models.IntegerField(blank=True, null=True)
    fb_reach = models.IntegerField(blank=True, null=True)
    fb_action_type_like = models.IntegerField(blank=True, null=True)
    fb_action_type_link_click = models.IntegerField(blank=True, null=True)
    fb_spend = models.FloatField(blank=True, null=True)
    fb_mobile_app_purchase_roas = models.FloatField(blank=True, null=True)
    fb_purchase_roas = models.FloatField(blank=True, null=True)
    fb_website_purchase_roas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_ai_predictions'


class JaAiPredictions1(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ecommerce_users = models.FloatField(blank=True, null=True)
    total_revenue = models.FloatField(blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)
    total_transactions = models.IntegerField(blank=True, null=True)
    avg_order_value = models.FloatField(blank=True, null=True)
    total_ads_clicks = models.IntegerField(blank=True, null=True)
    total_ads_cost = models.FloatField(blank=True, null=True)
    ads_cpc_value = models.FloatField(blank=True, null=True)
    mcf_conversion = models.FloatField(blank=True, null=True)
    mcf_conversion_value = models.FloatField(blank=True, null=True)
    mcf_assisted_conversion = models.FloatField(blank=True, null=True)
    mcf_assisted_value = models.FloatField(blank=True, null=True)
    social_facebook_clicks = models.IntegerField(blank=True, null=True)
    social_twitter_clicks = models.IntegerField(blank=True, null=True)
    social_pinterest_clicks = models.IntegerField(blank=True, null=True)
    social_instagram_clicks = models.IntegerField(blank=True, null=True)
    new_visitors = models.IntegerField(blank=True, null=True)
    returning_visitors = models.IntegerField(blank=True, null=True)
    total_users = models.IntegerField(blank=True, null=True)
    total_pageviews = models.IntegerField(blank=True, null=True)
    bounce_rate = models.FloatField(blank=True, null=True)
    total_sessions = models.IntegerField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True)
    session_by_desktop = models.FloatField(blank=True, null=True)
    session_by_tablet = models.FloatField(blank=True, null=True)
    session_by_mobile = models.FloatField(blank=True, null=True)
    total_mobile_users = models.IntegerField(blank=True, null=True)
    total_desktop_users = models.IntegerField(blank=True, null=True)
    total_tablet_users = models.IntegerField(blank=True, null=True)
    total_paid_pageviews = models.IntegerField(blank=True, null=True)
    total_paid_users = models.IntegerField(blank=True, null=True)
    total_referral_pageviews = models.IntegerField(blank=True, null=True)
    total_referral_users = models.IntegerField(blank=True, null=True)
    total_organic_pageviews = models.IntegerField(blank=True, null=True)
    total_organic_users = models.IntegerField(blank=True, null=True)
    total_direct_pageviews = models.IntegerField(blank=True, null=True)
    total_direct_users = models.IntegerField(blank=True, null=True)
    total_email_pageviews = models.IntegerField(blank=True, null=True)
    total_email_users = models.IntegerField(blank=True, null=True)
    fb_clicks = models.IntegerField(blank=True, null=True)
    fb_cpc = models.FloatField(blank=True, null=True)
    fb_impressions = models.IntegerField(blank=True, null=True)
    fb_reach = models.IntegerField(blank=True, null=True)
    fb_action_type_like = models.IntegerField(blank=True, null=True)
    fb_action_type_link_click = models.IntegerField(blank=True, null=True)
    fb_spend = models.FloatField(blank=True, null=True)
    fb_mobile_app_purchase_roas = models.FloatField(blank=True, null=True)
    fb_purchase_roas = models.FloatField(blank=True, null=True)
    fb_website_purchase_roas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_ai_predictions1'


class JaAiPredictions3(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ecommerce_users = models.FloatField(blank=True, null=True)
    total_revenue = models.FloatField(blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)
    total_transactions = models.IntegerField(blank=True, null=True)
    avg_order_value = models.FloatField(blank=True, null=True)
    total_ads_clicks = models.IntegerField(blank=True, null=True)
    total_ads_cost = models.FloatField(blank=True, null=True)
    ads_cpc_value = models.FloatField(blank=True, null=True)
    mcf_conversion = models.FloatField(blank=True, null=True)
    mcf_conversion_value = models.FloatField(blank=True, null=True)
    mcf_assisted_conversion = models.FloatField(blank=True, null=True)
    mcf_assisted_value = models.FloatField(blank=True, null=True)
    social_facebook_clicks = models.IntegerField(blank=True, null=True)
    social_twitter_clicks = models.IntegerField(blank=True, null=True)
    social_pinterest_clicks = models.IntegerField(blank=True, null=True)
    social_instagram_clicks = models.IntegerField(blank=True, null=True)
    new_visitors = models.IntegerField(blank=True, null=True)
    returning_visitors = models.IntegerField(blank=True, null=True)
    total_users = models.IntegerField(blank=True, null=True)
    total_pageviews = models.IntegerField(blank=True, null=True)
    bounce_rate = models.FloatField(blank=True, null=True)
    total_sessions = models.IntegerField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True)
    session_by_desktop = models.FloatField(blank=True, null=True)
    session_by_tablet = models.FloatField(blank=True, null=True)
    session_by_mobile = models.FloatField(blank=True, null=True)
    total_mobile_users = models.IntegerField(blank=True, null=True)
    total_desktop_users = models.IntegerField(blank=True, null=True)
    total_tablet_users = models.IntegerField(blank=True, null=True)
    total_paid_pageviews = models.IntegerField(blank=True, null=True)
    total_paid_users = models.IntegerField(blank=True, null=True)
    total_referral_pageviews = models.IntegerField(blank=True, null=True)
    total_referral_users = models.IntegerField(blank=True, null=True)
    total_organic_pageviews = models.IntegerField(blank=True, null=True)
    total_organic_users = models.IntegerField(blank=True, null=True)
    total_direct_pageviews = models.IntegerField(blank=True, null=True)
    total_direct_users = models.IntegerField(blank=True, null=True)
    total_email_pageviews = models.IntegerField(blank=True, null=True)
    total_email_users = models.IntegerField(blank=True, null=True)
    fb_clicks = models.IntegerField(blank=True, null=True)
    fb_cpc = models.FloatField(blank=True, null=True)
    fb_impressions = models.IntegerField(blank=True, null=True)
    fb_reach = models.IntegerField(blank=True, null=True)
    fb_action_type_like = models.IntegerField(blank=True, null=True)
    fb_action_type_link_click = models.IntegerField(blank=True, null=True)
    fb_spend = models.FloatField(blank=True, null=True)
    fb_mobile_app_purchase_roas = models.FloatField(blank=True, null=True)
    fb_purchase_roas = models.FloatField(blank=True, null=True)
    fb_website_purchase_roas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_ai_predictions3'


class JaAlexaInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=250)
    reach_rank = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    country_rank = models.CharField(max_length=150, blank=True, null=True)
    traffic_rank = models.CharField(max_length=150, blank=True, null=True)
    user_id = models.IntegerField()
    checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_alexa_info'


class JaAlexaInfoFull(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250)
    global_rank = models.CharField(max_length=20, blank=True, null=True)
    country_rank = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    traffic_rank_graph = models.TextField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)
    country_percent_visitor = models.TextField(blank=True, null=True)
    country_in_rank = models.TextField(blank=True, null=True)
    bounce_rate = models.CharField(max_length=20, blank=True, null=True)
    page_view_per_visitor = models.CharField(max_length=20, blank=True, null=True)
    daily_time_on_the_site = models.CharField(max_length=20, blank=True, null=True)
    visitor_percent_from_searchengine = models.CharField(max_length=20, blank=True, null=True)
    search_engine_percentage_graph = models.TextField(blank=True, null=True)
    keyword_name = models.TextField()
    keyword_percent_of_search_traffic = models.TextField(blank=True, null=True)
    upstream_site_name = models.TextField(blank=True, null=True)
    upstream_percent_unique_visits = models.TextField(blank=True, null=True)
    linking_in_site_name = models.TextField()
    total_site_linking_in = models.CharField(max_length=20, blank=True, null=True)
    linking_in_site_address = models.TextField(blank=True, null=True)
    subdomain_name = models.TextField(blank=True, null=True)
    subdomain_percent_visitors = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_alexa_info_full'


class JaAnalyticsError(models.Model):
    project_id = models.PositiveIntegerField()
    date = models.DateField()
    flag = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_analytics_error'


class JaAntivirusScanInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=250)
    google_status = models.CharField(max_length=100, blank=True, null=True)
    macafee_status = models.CharField(max_length=100, blank=True, null=True)
    avg_status = models.CharField(max_length=100, blank=True, null=True)
    norton_status = models.CharField(max_length=100, blank=True, null=True)
    scanned_at = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_antivirus_scan_info'


class JaBacklinkGenerator(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    url = models.TextField()
    domain_name = models.CharField(max_length=250)
    response_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10)
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    generated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_backlink_generator'


class JaBacklinkSearch(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250)
    backlink_count = models.CharField(max_length=100)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_backlink_search'


class JaCiSessions(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    timestamp = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ja_ci_sessions'


class JaCommonInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_code = models.CharField(max_length=200)
    reach_rank = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    country_rank = models.CharField(max_length=150, blank=True, null=True)
    traffic_rank = models.CharField(max_length=150, blank=True, null=True)
    dmoz_listed_or_not = models.IntegerField(blank=True, null=True)
    fb_total_share = models.CharField(max_length=150, blank=True, null=True)
    fb_total_like = models.CharField(max_length=150, blank=True, null=True)
    fb_total_comment = models.CharField(max_length=150, blank=True, null=True)
    g_back_link_count = models.CharField(max_length=150, blank=True, null=True)
    g_index_count = models.CharField(max_length=150, blank=True, null=True)
    g_page_rank = models.CharField(max_length=150, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    is_registered = models.CharField(max_length=150, blank=True, null=True)
    tech_email = models.CharField(max_length=150, blank=True, null=True)
    admin_email = models.CharField(max_length=150, blank=True, null=True)
    name_servers = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    sponsor = models.CharField(max_length=150, blank=True, null=True)
    changed_at = models.DateField(blank=True, null=True)
    expire_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_common_info'


class JaComparision(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    base_site = models.IntegerField()
    competutor_site = models.IntegerField()
    email = models.TextField()
    searched_at = models.DateTimeField()
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_comparision'


class JaCompatitorData(models.Model):
    site_url = models.TextField(blank=True, null=True)
    json_data = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_compatitor_data'


class JaConfig(models.Model):
    user_id = models.IntegerField()
    google_safety_api = models.TextField(blank=True, null=True)
    moz_access_id = models.CharField(max_length=100, blank=True, null=True)
    moz_secret_key = models.CharField(max_length=100, blank=True, null=True)
    mobile_ready_api_key = models.CharField(max_length=100)
    virus_total_api = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ja_config'


class JaConfigProxy(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    proxy = models.CharField(max_length=100, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    admin_permission = models.CharField(max_length=100)
    deleted = models.CharField(max_length=1)
    google_error = models.IntegerField(blank=True, null=True)
    bing_error = models.IntegerField(blank=True, null=True)
    yahoo_error = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    paid = models.IntegerField(blank=True, null=True)
    last_use = models.DateTimeField(blank=True, null=True)
    day_use_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_config_proxy'


class JaContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_contact_form'


class JaConversionSource(models.Model):
    source = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ja_conversion_source'


class JaConversionValue(models.Model):
    cs_id = models.IntegerField()
    project_management_id = models.IntegerField()
    date = models.DateField()
    total_conversion = models.IntegerField()
    conversion_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ja_conversion_value'


class JaCrons(models.Model):
    cron_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    last_used = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_crons'


class JaCurrency(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_currency'


class JaCurrencyPrice(models.Model):
    currency_code = models.CharField(max_length=10)
    price_against_usd = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ja_currency_price'


class JaDmozInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=150)
    listed_or_not = models.CharField(max_length=150, blank=True, null=True)
    user_id = models.IntegerField()
    checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_dmoz_info'


class JaDomain(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250)
    domain_code = models.CharField(max_length=250)
    js_code = models.TextField()
    table_name = models.TextField()
    add_date = models.DateField()
    dashboard = models.CharField(max_length=1)
    staff_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_domain'


class JaEmailConfig(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    email_address = models.CharField(max_length=100)
    smtp_host = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    smtp_user = models.CharField(max_length=100)
    smtp_password = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_email_config'


class JaEmailDirectories(models.Model):
    user_id = models.PositiveIntegerField()
    email = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    project_management_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_email_directories'


class JaExpiredDomainList(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=250, db_collation='latin1_swedish_ci', blank=True, null=True)
    auction_type = models.CharField(max_length=14, db_collation='latin1_swedish_ci', blank=True, null=True)
    auction_end_date = models.DateTimeField(blank=True, null=True)
    sync_at = models.DateField()
    page_rank = models.IntegerField(blank=True, null=True)
    google_index = models.CharField(max_length=15, db_collation='latin1_swedish_ci', blank=True, null=True)
    yahoo_index = models.CharField(max_length=15, db_collation='latin1_swedish_ci', blank=True, null=True)
    bing_index = models.CharField(max_length=15, db_collation='latin1_swedish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_expired_domain_list'


class JaFacebookAnalytics(models.Model):
    clicks = models.IntegerField()
    cpc = models.FloatField()
    cpm = models.FloatField()
    cpp = models.FloatField()
    impressions = models.IntegerField()
    reach = models.IntegerField()
    action_type_like = models.IntegerField()
    action_type_link_click = models.IntegerField()
    cost_per_unique_click = models.FloatField()
    unique_clicks = models.IntegerField()
    spend = models.FloatField()
    updated_date = models.DateField()
    account_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ja_facebook_analytics'


class JaFacebookCom1(models.Model):
    domain_id = models.IntegerField()
    domain_code = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    postal = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    device = models.CharField(max_length=250)
    browser_name = models.CharField(max_length=200)
    browser_version = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    referrer = models.CharField(max_length=200)
    visit_url = models.TextField()
    cookie_value = models.CharField(max_length=200)
    session_value = models.CharField(max_length=200)
    is_new = models.IntegerField()
    last_scroll_time = models.DateTimeField()
    last_engagement_time = models.DateTimeField()
    browser_rawdata = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ja_facebook_com_1'


class JaFallowLinks(models.Model):
    project_management_id = models.IntegerField()
    date = models.CharField(max_length=20, blank=True, null=True)
    do_follow = models.IntegerField(blank=True, null=True)
    no_follow = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_fallow_links'


class JaFbCurrencyCode(models.Model):
    project_management_id = models.IntegerField()
    currency_code = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ja_fb_currency_code'


class JaForgetPassword(models.Model):
    confirmation_code = models.CharField(max_length=15, db_collation='latin1_swedish_ci')
    email = models.CharField(max_length=100, db_collation='latin1_swedish_ci')
    success = models.IntegerField()
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_forget_password'


class JaFreshpluscarpetcareCom5(models.Model):
    domain_id = models.IntegerField()
    domain_code = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    postal = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    device = models.CharField(max_length=250)
    browser_name = models.CharField(max_length=200)
    browser_version = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    referrer = models.CharField(max_length=200)
    visit_url = models.TextField()
    cookie_value = models.CharField(max_length=200)
    session_value = models.CharField(max_length=200)
    is_new = models.IntegerField()
    last_scroll_time = models.DateTimeField()
    last_engagement_time = models.DateTimeField()
    browser_rawdata = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ja_freshpluscarpetcare_com_5'


class JaGAnalyticsData(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    ecommerce_users = models.FloatField(blank=True, null=True)
    total_revenue = models.FloatField(blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)
    total_transactions = models.IntegerField(blank=True, null=True)
    avg_order_value = models.FloatField(blank=True, null=True)
    total_ads_clicks = models.IntegerField(blank=True, null=True)
    total_ads_cost = models.FloatField(blank=True, null=True)
    ads_cpc_value = models.FloatField(blank=True, null=True)
    mcf_conversion = models.FloatField(blank=True, null=True)
    mcf_conversion_value = models.FloatField(blank=True, null=True)
    mcf_assisted_conversion = models.FloatField(blank=True, null=True)
    mcf_assisted_value = models.FloatField(blank=True, null=True)
    social_facebook_clicks = models.IntegerField(blank=True, null=True)
    social_twitter_clicks = models.IntegerField(blank=True, null=True)
    social_pinterest_clicks = models.IntegerField(blank=True, null=True)
    social_instagram_clicks = models.IntegerField(blank=True, null=True)
    new_visitors = models.IntegerField(blank=True, null=True)
    returning_visitors = models.IntegerField(blank=True, null=True)
    total_users = models.IntegerField(blank=True, null=True)
    total_pageviews = models.IntegerField(blank=True, null=True)
    bounce_rate = models.FloatField(blank=True, null=True)
    total_sessions = models.IntegerField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True)
    session_by_desktop = models.FloatField(blank=True, null=True)
    session_by_tablet = models.FloatField(blank=True, null=True)
    session_by_mobile = models.FloatField(blank=True, null=True)
    total_mobile_users = models.IntegerField(blank=True, null=True)
    total_desktop_users = models.IntegerField(blank=True, null=True)
    total_tablet_users = models.IntegerField(blank=True, null=True)
    total_paid_pageviews = models.IntegerField(blank=True, null=True)
    total_paid_users = models.IntegerField(blank=True, null=True)
    total_referral_pageviews = models.IntegerField(blank=True, null=True)
    total_referral_users = models.IntegerField(blank=True, null=True)
    total_organic_pageviews = models.IntegerField(blank=True, null=True)
    total_organic_users = models.IntegerField(blank=True, null=True)
    total_direct_pageviews = models.IntegerField(blank=True, null=True)
    total_direct_users = models.IntegerField(blank=True, null=True)
    total_email_pageviews = models.IntegerField(blank=True, null=True)
    total_email_users = models.IntegerField(blank=True, null=True)
    fb_clicks = models.IntegerField(blank=True, null=True)
    fb_cpc = models.FloatField(blank=True, null=True)
    fb_impressions = models.IntegerField(blank=True, null=True)
    fb_reach = models.IntegerField(blank=True, null=True)
    fb_action_type_like = models.IntegerField(blank=True, null=True)
    fb_action_type_link_click = models.IntegerField(blank=True, null=True)
    fb_spend = models.FloatField(blank=True, null=True)
    fb_mobile_app_purchase_roas = models.FloatField(blank=True, null=True)
    fb_purchase_roas = models.FloatField(blank=True, null=True)
    fb_website_purchase_roas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_g_analytics_data'


class JaGoogleAdword(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    keyword = models.CharField(max_length=250)
    location = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    proxy = models.TextField(blank=True, null=True)
    title = models.TextField(db_collation='latin1_swedish_ci')
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    scraped_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_google_adword'


class JaGoogleSheets(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    uri = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField()
    project_management_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    sheet_category = models.IntegerField(blank=True, null=True)
    is_published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_google_sheets'


class JaGoogleplusInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_id = models.CharField(max_length=150)
    share_count = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ja_googleplus_info'


class JaHistoryLog(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    staff_id = models.PositiveIntegerField(blank=True, null=True)
    project_management_id = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_history_log'


class JaIpCountryList(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    ip_range_start = models.CharField(max_length=15, blank=True, null=True)
    ip_range_end = models.CharField(max_length=15, blank=True, null=True)
    ip_range_start_int = models.IntegerField(blank=True, null=True)
    ip_range_end_int = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=15, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_ip_country_list'


class JaIpDomainInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    isp = models.CharField(max_length=100, blank=True, null=True)
    domain_name = models.CharField(max_length=250)
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    time_zone = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_ip_domain_info'


class JaIpInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_id = models.CharField(max_length=150)
    isp = models.CharField(max_length=150)
    ip = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    time_zone = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    latitude = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ja_ip_info'


class JaIpSameSite(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_ip_same_site'


class JaIpV6Check(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    ipv6 = models.CharField(max_length=200, blank=True, null=True)
    searched_at = models.DateTimeField()
    ip = models.CharField(max_length=200, blank=True, null=True)
    is_ipv6_support = models.CharField(max_length=10)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_ip_v6_check'


class JaJustanchorCom5(models.Model):
    domain_id = models.IntegerField()
    domain_code = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    postal = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    device = models.CharField(max_length=250)
    browser_name = models.CharField(max_length=200)
    browser_version = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    referrer = models.CharField(max_length=200)
    visit_url = models.TextField()
    cookie_value = models.CharField(max_length=200)
    session_value = models.CharField(max_length=200)
    is_new = models.IntegerField()
    last_scroll_time = models.DateTimeField()
    last_engagement_time = models.DateTimeField()
    browser_rawdata = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ja_justanchor_com_5'


class JaKeys(models.Model):
    key = models.CharField(max_length=40)
    level = models.IntegerField()
    ignore_limits = models.IntegerField()
    is_private_key = models.IntegerField()
    ip_addresses = models.TextField(blank=True, null=True)
    date_created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_keys'


class JaKeywordPosition(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250)
    keyword = models.CharField(max_length=250)
    location = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    proxy = models.TextField(blank=True, null=True)
    google_position = models.CharField(max_length=100, blank=True, null=True)
    google_top_site_url = models.TextField(blank=True, null=True)
    bing_position = models.CharField(max_length=100, blank=True, null=True)
    bing_top_site_url = models.TextField(blank=True, null=True)
    yahoo_position = models.CharField(max_length=100, blank=True, null=True)
    yahoo_top_site_url = models.TextField(blank=True, null=True)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_keyword_position'


class JaKeywordPositionReport(models.Model):
    keyword_id = models.IntegerField()
    date = models.DateField()
    google_position = models.IntegerField(blank=True, null=True)
    bing_position = models.CharField(max_length=100, blank=True, null=True)
    yahoo_position = models.CharField(max_length=100, blank=True, null=True)
    meta_title = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    m_position = models.IntegerField(blank=True, null=True)
    m_title = models.CharField(max_length=500, blank=True, null=True)
    m_description = models.CharField(max_length=500, blank=True, null=True)
    m_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_keyword_position_report'


class JaKeywordPositionSet(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=250)
    website = models.CharField(max_length=250, db_collation='latin1_swedish_ci')
    language = models.CharField(max_length=250, db_collation='latin1_swedish_ci')
    country = models.CharField(max_length=250, db_collation='latin1_swedish_ci')
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    add_date = models.DateTimeField()
    desktop_flag = models.IntegerField(blank=True, null=True)
    mobile_flag = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    deleted = models.IntegerField()
    keyword_sv_tracked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_keyword_position_set'


class JaKeywordSearchVolume(models.Model):
    keyword_id = models.IntegerField()
    cmp = models.FloatField(blank=True, null=True)
    cpc = models.FloatField(blank=True, null=True)
    sv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_keyword_search_volume'


class JaKeywordSearchVolumeMonthly(models.Model):
    keyword_id = models.IntegerField()
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_keyword_search_volume_monthly'


class JaKeywordSuggestion(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=100)
    google_suggestion = models.TextField(blank=True, null=True)
    bing_suggestion = models.TextField(blank=True, null=True)
    yahoo_suggestion = models.TextField(blank=True, null=True)
    wiki_suggestion = models.TextField(blank=True, null=True)
    amazon_suggestion = models.TextField(blank=True, null=True)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_keyword_suggestion'


class JaKeywordToCategory(models.Model):
    keyword_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_keyword_to_category'


class JaLinkAnalysis(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    url = models.TextField()
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    external_link_count = models.CharField(max_length=50, blank=True, null=True)
    internal_link_count = models.CharField(max_length=50, blank=True, null=True)
    nofollow_count = models.CharField(max_length=50, blank=True, null=True)
    do_follow_count = models.CharField(max_length=50, blank=True, null=True)
    external_link = models.TextField(blank=True, null=True)
    internal_link = models.TextField(blank=True, null=True)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_link_analysis'


class JaLoginConfig(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    app_name = models.CharField(max_length=100, blank=True, null=True)
    api_id = models.CharField(max_length=250, blank=True, null=True)
    api_secret = models.CharField(max_length=250, blank=True, null=True)
    google_client_id = models.TextField(blank=True, null=True)
    google_client_secret = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_login_config'


class JaLogs(models.Model):
    id = models.IntegerField()
    uri = models.CharField(max_length=255)
    method = models.CharField(max_length=6)
    params = models.TextField(blank=True, null=True)
    api_key = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=45)
    time = models.IntegerField()
    rtime = models.FloatField(blank=True, null=True)
    authorized = models.CharField(max_length=1)
    response_code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_logs'


class JaMenu(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    serial = models.IntegerField()
    module_access = models.CharField(max_length=255)
    have_child = models.CharField(max_length=1)
    only_admin = models.CharField(max_length=1)
    only_member = models.CharField(max_length=1)
    add_ons_id = models.IntegerField()
    is_external = models.CharField(max_length=1)
    seo_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_menu'


class JaMenuChild1(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    serial = models.IntegerField()
    icon = models.CharField(max_length=255)
    module_access = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    have_child = models.CharField(max_length=1)
    only_admin = models.CharField(max_length=1)
    only_member = models.CharField(max_length=1)
    is_external = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_menu_child_1'


class JaMenuChild2(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    serial = models.IntegerField()
    icon = models.CharField(max_length=255)
    module_access = models.CharField(max_length=255)
    parent_child = models.IntegerField()
    only_admin = models.CharField(max_length=1)
    only_member = models.CharField(max_length=1)
    is_external = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_menu_child_2'


class JaMenuExtra(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    original_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_menu_extra'


class JaMetaTagInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_id = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField()
    keywords = models.TextField()
    language = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ja_meta_tag_info'


class JaModules(models.Model):
    module_name = models.CharField(max_length=250, db_collation='latin1_swedish_ci', blank=True, null=True)
    add_ons_id = models.IntegerField()
    extra_text = models.CharField(max_length=50)
    limit_enabled = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_modules'


class JaMozInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    url = models.TextField()
    mozrank_subdomain_normalized = models.CharField(max_length=150)
    mozrank_subdomain_raw = models.CharField(max_length=150)
    mozrank_url_normalized = models.CharField(max_length=150)
    mozrank_url_raw = models.CharField(max_length=150)
    http_status_code = models.CharField(max_length=150)
    domain_authority = models.CharField(max_length=150)
    page_authority = models.CharField(max_length=150)
    external_equity_links = models.CharField(max_length=150)
    links = models.CharField(max_length=150)
    user_id = models.IntegerField()
    checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_moz_info'


class JaNativeApi(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    api_key = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ja_native_api'


class JaNonVerifiedProjects(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_non_verified_projects'


class JaNotifications(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField()
    project_management_id = models.IntegerField()
    read = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_notifications'


class JaOffpageKeywords(models.Model):
    keyword = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    project_management_id = models.IntegerField()
    keyword_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_offpage_keywords'


class JaPackage(models.Model):
    package_name = models.CharField(max_length=250)
    module_ids = models.CharField(max_length=250, db_collation='latin1_swedish_ci')
    monthly_limit = models.TextField(blank=True, null=True)
    bulk_limit = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    validity = models.IntegerField()
    is_default = models.CharField(max_length=1)
    package_type = models.IntegerField()
    deleted = models.CharField(max_length=1, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'ja_package'


class JaPageStatus(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    url = models.TextField()
    user_id = models.CharField(max_length=222, db_collation='latin1_swedish_ci')
    http_code = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    status = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    total_time = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    namelookup_time = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    connect_time = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    speed_download = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    check_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_page_status'


class JaPageanalysis(models.Model):
    domain = models.CharField(max_length=255, blank=True, null=True)
    compare = models.IntegerField()
    base_site = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    project_management_id = models.IntegerField(blank=True, null=True)
    is_processing = models.IntegerField(blank=True, null=True)
    is_done = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_pageanalysis'


class JaPaymentConfig(models.Model):
    paypal_email = models.CharField(max_length=250)
    stripe_secret_key = models.CharField(max_length=150)
    stripe_publishable_key = models.CharField(max_length=150)
    currency = models.CharField(max_length=3)
    deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ja_payment_config'


class JaPlagarism(models.Model):
    user_id = models.PositiveIntegerField()
    project_management_id = models.PositiveIntegerField()
    urls = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    is_processing = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_plagarism'


class JaProjectCat(models.Model):
    name = models.CharField(max_length=255)
    have_childs = models.CharField(max_length=1, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_project_cat'


class JaProjectCategory(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_project_category'


class JaProjectManagement(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    main_cat = models.CharField(max_length=255, blank=True, null=True)
    child_cat = models.CharField(max_length=255, blank=True, null=True)
    currency_id = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField()
    dashboard_type = models.CharField(max_length=255, blank=True, null=True)
    google_keyword_sheet = models.CharField(max_length=255, blank=True, null=True)
    google_keyword_sheet_created = models.IntegerField(blank=True, null=True)
    project_management_link = models.CharField(max_length=300, blank=True, null=True)
    slack_channel_link = models.CharField(max_length=300, blank=True, null=True)
    fb_account_id = models.CharField(max_length=80, blank=True, null=True)
    fb_app_id = models.CharField(max_length=80, blank=True, null=True)
    fb_app_secret = models.CharField(max_length=200, blank=True, null=True)
    fb_access_token = models.CharField(max_length=200, blank=True, null=True)
    ai_flag = models.IntegerField(blank=True, null=True)
    ecommerce_analytics = models.IntegerField(blank=True, null=True)
    google_ads_data = models.IntegerField(blank=True, null=True)
    user_analytics = models.IntegerField(blank=True, null=True)
    traffic_analytics = models.IntegerField(blank=True, null=True)
    facebook_roas_data = models.IntegerField(blank=True, null=True)
    facebook_ads_data = models.IntegerField(blank=True, null=True)
    mcf_conversion_data = models.IntegerField(blank=True, null=True)
    google_webmasters_keywords = models.IntegerField(blank=True, null=True)
    active_users_location = models.IntegerField()
    active_pages_custom_chart = models.IntegerField()
    seo_data_google_serps = models.IntegerField()
    age_group_data = models.IntegerField()
    count_of_sessions = models.IntegerField()
    ssl_flag = models.IntegerField()
    sitemap = models.IntegerField()
    mobile_speed = models.CharField(max_length=50, blank=True, null=True)
    desktop_speed = models.CharField(max_length=50, blank=True, null=True)
    keyword_position_status = models.IntegerField()
    shopify_tokan = models.CharField(max_length=500, blank=True, null=True)
    keyword_frequency = models.IntegerField(blank=True, null=True)
    follow_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_project_management'


class JaPublicProxy(models.Model):
    ip = models.CharField(max_length=100)
    proxy_type = models.CharField(max_length=7, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    google_error = models.IntegerField(blank=True, null=True)
    yahoo_error = models.IntegerField(blank=True, null=True)
    bing_error = models.IntegerField(blank=True, null=True)
    last_use = models.DateTimeField(blank=True, null=True)
    day_use_total = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    speed = models.CharField(max_length=100, blank=True, null=True)
    alive = models.CharField(max_length=30, blank=True, null=True)
    proxy_status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_public_proxy'


class JaRapidPestcontrolCom5(models.Model):
    domain_id = models.IntegerField()
    domain_code = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    postal = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    device = models.CharField(max_length=250)
    browser_name = models.CharField(max_length=200)
    browser_version = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    referrer = models.CharField(max_length=200)
    visit_url = models.TextField()
    cookie_value = models.CharField(max_length=200)
    session_value = models.CharField(max_length=200)
    is_new = models.IntegerField()
    last_scroll_time = models.DateTimeField()
    last_engagement_time = models.DateTimeField()
    browser_rawdata = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ja_rapid-pestcontrol_com_5'


class JaSaveStudent19(models.Model):
    domain_id = models.IntegerField()
    domain_code = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    postal = models.CharField(max_length=250)
    os = models.CharField(max_length=250)
    device = models.CharField(max_length=250)
    browser_name = models.CharField(max_length=200)
    browser_version = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    referrer = models.CharField(max_length=200)
    visit_url = models.TextField()
    cookie_value = models.CharField(max_length=200)
    session_value = models.CharField(max_length=200)
    is_new = models.IntegerField()
    last_scroll_time = models.DateTimeField()
    last_engagement_time = models.DateTimeField()
    browser_rawdata = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ja_save student_19'


class JaSearchEngineIndex(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=250, db_collation='utf8_general_ci')
    google_index = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    bing_index = models.CharField(max_length=20, blank=True, null=True)
    yahoo_index = models.CharField(max_length=20, blank=True, null=True)
    checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_search_engine_index'


class JaSearchEnginePageRank(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250, db_collation='utf8_general_ci')
    google_page_rank = models.CharField(max_length=20, blank=True, null=True)
    checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_search_engine_page_rank'


class JaSearchEngines(models.Model):
    se_id = models.AutoField(primary_key=True)
    se_name = models.CharField(max_length=400, blank=True, null=True)
    se_country_iso_code = models.CharField(max_length=30, blank=True, null=True)
    se_country_name = models.CharField(max_length=200, blank=True, null=True)
    se_language = models.CharField(max_length=300, blank=True, null=True)
    se_localization = models.CharField(max_length=200, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_search_engines'


class JaSearchEnginesLocs(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_id_parent = models.CharField(max_length=20, blank=True, null=True)
    loc_name = models.CharField(max_length=200, blank=True, null=True)
    loc_name_canonical = models.CharField(max_length=500, blank=True, null=True)
    loc_type = models.CharField(max_length=200, blank=True, null=True)
    loc_country_iso_code = models.CharField(max_length=20, blank=True, null=True)
    dma_region = models.CharField(max_length=4, blank=True, null=True)
    kwrd_finder = models.CharField(max_length=4, blank=True, null=True)
    kwrd_finder_lang = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_search_engines_locs'


class JaSheetCategories(models.Model):
    type = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=255)
    user_id = models.IntegerField()
    project_management_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_sheet_categories'


class JaSheetCategories1(models.Model):
    type = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=255)
    user_id = models.IntegerField()
    project_management_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ja_sheet_categories1'


class JaSimilarWebInfo(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    domain_name = models.CharField(max_length=250)
    global_rank = models.CharField(max_length=20, blank=True, null=True)
    country_rank = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    category_rank = models.CharField(max_length=20, blank=True, null=True)
    total_visit = models.CharField(max_length=50, blank=True, null=True)
    time_on_site = models.CharField(max_length=50, blank=True, null=True)
    page_views = models.CharField(max_length=50, blank=True, null=True)
    traffic_country = models.TextField(blank=True, null=True)
    traffic_country_percentage = models.TextField(blank=True, null=True)
    direct_traffic = models.CharField(max_length=50, blank=True, null=True)
    referral_traffic = models.CharField(max_length=50, blank=True, null=True)
    search_traffic = models.CharField(max_length=50, blank=True, null=True)
    social_traffic = models.CharField(max_length=50, blank=True, null=True)
    mail_traffic = models.CharField(max_length=50, blank=True, null=True)
    display_traffic = models.CharField(max_length=50, blank=True, null=True)
    top_referral_site = models.TextField(blank=True, null=True)
    top_destination_site = models.TextField(blank=True, null=True)
    organic_search_percentage = models.CharField(max_length=20, blank=True, null=True)
    paid_search_percentage = models.CharField(max_length=20, blank=True, null=True)
    top_organic_keyword = models.TextField(blank=True, null=True)
    top_paid_keyword = models.TextField(blank=True, null=True)
    social_site_name = models.TextField(blank=True, null=True)
    social_site_percentage = models.TextField(blank=True, null=True)
    bounce_rate = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20)
    searched_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ja_similar_web_info'


class JaSiteCheckReport(models.Model):
    project_management_id = models.IntegerField(blank=True, null=True)
    domain_name = models.CharField(max_length=200, blank=True, null=True)
    searched_at = models.DateTimeField()
    response_code = models.CharField(max_length=50, blank=True, null=True)
    speed_score = models.CharField(max_length=50, blank=True, null=True)
    pagestat = models.TextField(blank=True, null=True)
    avoid_landing_page_redirects = models.TextField(blank=True, null=True)
    gzip_compression = models.TextField(blank=True, null=True)
    leverage_browser_caching = models.TextField(blank=True, null=True)
    main_resource_server_response_time = models.TextField(blank=True, null=True)
    minify_css = models.TextField(blank=True, null=True)
    minify_html = models.TextField(blank=True, null=True)
    minify_javascript = models.TextField(db_column='minify_javaScript', blank=True, null=True)  # Field name made lowercase.
    minimize_render_blocking_resources = models.TextField(blank=True, null=True)
    optimize_images = models.TextField(blank=True, null=True)
    prioritize_visible_content = models.TextField(blank=True, null=True)
    response_code_mobile = models.CharField(max_length=50, blank=True, null=True)
    speed_score_mobile = models.CharField(max_length=50, blank=True, null=True)
    speed_usability_mobile = models.CharField(max_length=50, blank=True, null=True)
    pagestat_mobile = models.TextField(blank=True, null=True)
    avoid_interstitials_mobile = models.TextField(blank=True, null=True)
    avoid_plugins_mobile = models.TextField(blank=True, null=True)
    configure_viewport_mobile = models.TextField(blank=True, null=True)
    size_content_to_viewport_mobile = models.TextField(blank=True, null=True)
    size_tap_targets_appropriately_mobile = models.TextField(blank=True, null=True)
    use_legible_font_sizes_mobile = models.TextField(blank=True, null=True)
    avoid_landing_page_redirects_mobile = models.TextField(blank=True, null=True)
    gzip_compression_mobile = models.TextField(blank=True, null=True)
    leverage_browser_caching_mobile = models.TextField(blank=True, null=True)
    main_resource_server_response_time_mobile = models.TextField(blank=True, null=True)
    minify_css_mobile = models.TextField(blank=True, null=True)
    minify_html_mobile = models.TextField(blank=True, null=True)
    minify_javascript_mobile = models.TextField(db_column='minify_javaScript_mobile', blank=True, null=True)  # Field name made lowercase.
    minimize_render_blocking_resources_mobile = models.TextField(blank=True, null=True)
    optimize_images_mobile = models.TextField(blank=True, null=True)
    prioritize_visible_content_mobile = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    viewport = models.CharField(max_length=50, blank=True, null=True)
    h1 = models.TextField(blank=True, null=True)
    h2 = models.TextField(blank=True, null=True)
    h3 = models.TextField(blank=True, null=True)
    h4 = models.TextField(blank=True, null=True)
    h5 = models.TextField(blank=True, null=True)
    h6 = models.TextField(blank=True, null=True)
    noindex_by_meta_robot = models.CharField(max_length=50, blank=True, null=True)
    nofollowed_by_meta_robot = models.CharField(max_length=50, blank=True, null=True)
    keyword_one_phrase = models.TextField(blank=True, null=True)
    keyword_two_phrase = models.TextField(blank=True, null=True)
    keyword_three_phrase = models.TextField(blank=True, null=True)
    keyword_four_phrase = models.TextField(blank=True, null=True)
    total_words = models.CharField(max_length=50, blank=True, null=True)
    robot_txt_exist = models.CharField(max_length=50, blank=True, null=True)
    robot_txt_content = models.TextField(blank=True, null=True)
    sitemap_exist = models.CharField(max_length=50, blank=True, null=True)
    sitemap_location = models.TextField(blank=True, null=True)
    external_link_count = models.CharField(max_length=50, blank=True, null=True)
    internal_link_count = models.CharField(max_length=50, blank=True, null=True)
    nofollow_link_count = models.CharField(max_length=50, blank=True, null=True)
    dofollow_link_count = models.CharField(max_length=50, blank=True, null=True)
    external_link = models.TextField(blank=True, null=True)
    internal_link = models.TextField(blank=True, null=True)
    nofollow_internal_link = models.TextField(blank=True, null=True)
    not_seo_friendly_link = models.TextField(blank=True, null=True)
    image_without_alt_count = models.CharField(max_length=50, blank=True, null=True)
    image_not_alt_list = models.TextField(blank=True, null=True)
    inline_css = models.TextField(blank=True, null=True)
    internal_css = models.TextField(blank=True, null=True)
    depreciated_html_tag = models.TextField(blank=True, null=True)
    is_favicon_found = models.CharField(max_length=50, blank=True, null=True)
    favicon_link = models.CharField(max_length=50, blank=True, null=True)
    total_page_size_general = models.CharField(max_length=50, blank=True, null=True)
    page_size_gzip = models.CharField(max_length=50, blank=True, null=True)
    is_gzip_enable = models.CharField(max_length=50, blank=True, null=True)
    doctype = models.CharField(max_length=50, blank=True, null=True)
    doctype_is_exist = models.CharField(max_length=50, blank=True, null=True)
    nofollow_link_list = models.TextField(blank=True, null=True)
    canonical_link_list = models.TextField(blank=True, null=True)
    noindex_list = models.TextField(blank=True, null=True)
    micro_data_schema_list = models.TextField(blank=True, null=True)
    is_ipv6_compatiable = models.CharField(max_length=50, blank=True, null=True)
    ipv6 = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    dns_report = models.TextField(blank=True, null=True)
    is_ip_canonical = models.CharField(max_length=50, blank=True, null=True)
    email_list = models.TextField(blank=True, null=True)
    is_url_canonicalized = models.CharField(max_length=50, blank=True, null=True)
    text_to_html_ratio = models.CharField(max_length=50, blank=True, null=True)
    general_curl_response = models.TextField(blank=True, null=True)
    mobile_ready_data = models.TextField(blank=True, null=True)
    warning_count = models.CharField(max_length=50, blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    domain_ip_info = models.TextField(blank=True, null=True)
    alexa_rank = models.TextField(blank=True, null=True)
    overall_score = models.FloatField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ja_site_check_report'
