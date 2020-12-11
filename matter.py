# from suitetail import NetSuite
# from netsuite_service import NetSuiteService

from lib.rocket_matter import RocketMatter
# from lib.config import Config

class Matter:

	def sync(self):
		"""Sync all matters"""

		# NetSuite().reset_token()
		print('Syncing matters')
		service = RocketMatter()
		service.service_name = 'Matters'
		service.table_name = 'matters'
		service.child_mappings = {
			"MatterType" : {
				"table": "matter_types",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					"Name": "name",
					"ID": "id",
				}
			},

			"MatterEverGreenInfo" : {
				"table": "matter_ever_green_info",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					"IsOn": "is_on",
					"MinimumRequiredRetainer": "minimum_required_retainer",
					"ReplenishWhenBelow": "replenish_when_below",
				}
			},

			"RelatedContacts" : {
				"table": "matter_related_contacts",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"ContactId": "contact_id",
					"MatterID": "matter_id",
					"ID": "id",
					"Role": "role",
					"Position": "position",
					"RelationshipName": "relationship_name",
					"IsDefault": "is_default",
					"IsUser": "is_user",
					"IsAttendeeRole": "is_attendee_role",
					"IsEventOwnerRole": "is_event_owner_role",
					"TaskAssigneeRole": "task_assignee_role",
					"TaskOwnerRole": "task_owner_role",
				}
			},

			"CustomFields" : {
				"table": "matter_custom_fields",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					'ID': 'id',
					"parent_id": "matter_id",
					'Name': 'name',
					'Value': 'value',
					'Position': 'position',
				}
			},

			"MatterPermissionType" : {
				"table": "matter_permission_types",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					'ID': 'id',
					'Name': 'name'
				}
			},

			"Permissions" : {
				"table": "matter_permissions",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"MatterID": "matter_id",
					'ID': 'id',
					'UserID': 'user_id',
					'UserFullName': 'user_full_name'
				}
			},

			"Events" : {
				"table": "matter_events",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"ParentEventId": "parent_event_id",
					"MatterID": "matter_id",
					"MatterName": "matter_name",
					"Title": "title",
					"Notes": "notes",
					"Location": "location",
					"StartDateString": "start_date_string",
					"StartDate": "start_date",
					"StartDay": "start_day",
					"StartTime": "start_time",
					"EndDay": "end_day",
					"EndTime": "end_time",
					"EndDateString": "end_date_string",
					"EndDate": "end_date",
					"BillingDate": "billing_date",
					"OwnerID": "owner_id",
					"OwnerName": "string",
					"Bill": "bill",
					"NonBillable": "non_billable",
					"IsMilestonePending": "is_milestone_pending",
					"ActivityId": "activity_id",
					"IsPrivate": "is_private",
					"IsFlagged": "is_flagged",
					"IsAllDayEvent": "is_all_day_event",
					"IsRecurringEvent": "is_recurring_event",
					"RemindParticipants": "remind_participants",
					"ReminderInterval": "reminder_interval",
					"RecurringFrequency": "recurring_frequency",
					"RecurringInterval": "recurring_interval",
					"RecurringEventEndType": "recurring_event_end_type",
					"ReminderIntervalType": "reminder_interval_type",
					"RecurringEventEndDate": "recurring_event_end_date",
					"ReminderDate": "reminder_date",
					"RecurringEventOccurences": "recurring_event_occurences",
					"OwnerIsRole": "owner_is_role",
					"OwnerRole": "owner_role",
					"IsInvoiced": "is_invoiced",
					"WebLink": "web_link",
					"IsCourtRule": "is_court_rule",
					"MatterCourtRuleId": "matter_court_rule_id",
					"ThirdPartyDeadlineId": "third_party_deadline_id",
					"IsStatute": "is_statute",
				}
			},

			"Tasks" : {
				"table": "matter_tasks",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					'ID': 'id',
					'MatterID': 'matter_id',
					'Title': 'title',
					'DueDate': 'due_date',
					'OwnerID': 'owner_id',
					'AssignedToID': 'assigned_to_id',
					'Position': 'position',
					'MatterPosition': 'matter_position',
					'MatterTemplateMilestoneActionId': 'matter_temp_ml_action_id',
					'IsMilestonePending': 'is_milestone_pending',
					'IsComplete': 'is_complete',
					'ActivityId': 'activity_id',
					'IsRead': 'is_read',
					'Invoiced': 'invoiced',
					'PendingInvoicing': 'pending_invoicing',
					'BillingDate': 'billing_date',
					'TotalSeconds': 'total_seconds',
					'BillableUnits': 'billable_units',
					'Notes': 'notes',
					'Cost': 'cost',
					'IsNoCharge': 'is_nocharge',
					'IsNonBillable': 'is_non_billable',
					'CompletedDate': 'completed_date',
					'OwnerIsRole': 'owner_is_role',
					'AssignedToIsRole': 'assigned_to_is_role',
					'OwnerRole': 'owner_role',
					'AssignedToRole': 'assigned_to_role',
				}
			},

			"StatueOfLimitation" : {
				"table": "matter_statue_of_limitation",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					'DoesNotExpire': 'does_not_expire',
					'ExpirationDate': 'expiration_date'
				}
			},

			"ShareInvoicesAutomaticallyWith" : {
				"table": "matter_share_inv_auto_with",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					"ID": "id",
					"Name": "name",
					"Code": "code",
					"MiddleName": "middle_name",
					"LastName": "last_name",
					"IsCompany": "is_company",
					"ContactID": "contact_id",
					"CompanyID": "company_id",
					"CompanyName": "company_name",
					"WorkEmail": "work_email",
					"FullName": "full_name",
					"HomeEmail": "home_email",
					"MobilePhone": "mobile_phone",
					"Notes": "notes",
					"PreferredDisplayName": "preferred_display_name",
					"PrimaryContact": "primary_contact",
					"PrimaryContactId": "primary_contact_id",
					"Salutation": "salutation",
					"SkypeUserName": "skype_user_name",
					"Suffix": "suffix",
					"Title": "title",
					"WorkFax": "work_fax",
					"WorkPhone": "work_phone",
					"HomePhone": "home_phone",
					"WorkPhoneExt": "work_phone_ext",
				}
			},

			"ShareInvoiceSettings" : {
				"table": "matter_share_inv_with_settings",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					"ContactID": "contact_id",
					"FullName": "full_name",
					"ShareByPortal": "share_by_portal",
					"ShareByEmail": "share_by_email",
					"EmailTypeSelected": "email_type_selected",
					"ID": "id"
				}
			},

			"MatterBudget" : {
				"table": "matter_budget",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"Id": "id",
					"MatterID": "matter_id",
					"Budget": "budget",
					"IsEnabled": "is_enabled",
					"IncludeTimeEntries": "include_time_entries",
					"IncludeFlatFeeEntries": "include_flat_fee_entries",
					"IncludeCosts": "include_costs",
					"UseUserDefaultRate": "use_user_default_rate",
					"ExcludeInvoiced": "exclude_invoiced",
				}
			},

			"Client" : {
				"table": "matter_clients",
				"mapping_table": "",
				"columns": {
					'data_inserted_from': 'data_inserted_from',
					'ez_created_on': 'ez_created_on',
					"parent_id": "matter_id",
					"ID": "id",
					"Name": "name",
					"Code": "code",
					"MiddleName": "middle_name",
					"LastName": "last_name",
					"IsCompany": "is_company",
					"ContactID": "contact_id",
					"CompanyID": "company_id",
					"CompanyName": "company_name",
					"WorkEmail": "work_email",
					"FullName": "full_name",
					"HomeEmail": "home_email",
					"MobilePhone": "mobile_phone",
					"Notes": "notes",
					"PreferredDisplayName": "preferred_display_name",
					"PrimaryContact": "primary_contact",
					"PrimaryContactId": "primary_contact_id",
					"Salutation": "salutation",
					"SkypeUserName": "skype_user_name",
					"Suffix": "suffix",
					"Title": "title",
					"WorkFax": "work_fax",
					"WorkPhone": "work_phone",
					"HomePhone": "home_phone",
					"WorkPhoneExt": "work_phone_ext",
				}
			},




		}

		service.column_mappings = {
			"data_inserted_from": "data_inserted_from",
			"ez_created_on": "ez_created_on",
			"ID": "id",
			"Description": "description",
			"OpenDate": "open_date",
			"ClosedDate": "closed_date",
			"CompletedDate": "completed_date",
			"EmailFolder": "email_folder",
			"MatterWorkFlowStatusId": "matter_work_flow_status_id",
			"Name": "name",
			"ClientMatter": "client_matter",
			"TaxRateId": "tax_rate_id",
			"DiscountRateId": "discount_rate_id",
			"InterestRateId": "interest_rate_id",
			"SurchargeRateId": "surcharge_rate_id",
			"FlatFeeOf": "flat_fee_of",
			"MatterPermissionTypeID": "matter_permission_type_id",
			"PrimaryAttorneyContactID": "primary_attorney_contact_id",
			"InvoiceTemplateId": "invoice_template_id",
			"PaymentProcessingFeePercent": "payment_processing_fee_percent",
			"SurchargeHistoryId": "surcharge_history_id",
			"MatterTemplateId": "matter_template_id",
			"MatterTypeID": "matter_type_id",
			"MatterStatusTypeId": "matter_status_type_id",
			"DefaultBillingTypeId": "default_billing_type_id",
			"IsSystemMatter": "is_system_matter",
			"EnablePaymentProcessingFee": "enable_payment_processing_fee",
			"EnableSurchargeFee": "enable_surcharge_fee",
			"IsPendingImport": "is_pending_import",
			"FireTemplateSelection": "fire_template_selection",

		}
		service.api_url = 'API_V2/Matters.svc/json/GetMattersBySearch'
		service.specific_api = {'endpoint': 'API_V2/Matters.svc/json/Get', 'name': 'Matter', 'param': 'ID',
            "request": {
                "ID": 0
            }}
		service.process_listing()


'''
Import matters
'''
if __name__ == '__main__':
	Matter().sync()