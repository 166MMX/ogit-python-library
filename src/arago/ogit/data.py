from typing import Generator

from arago.ontology import Scope, Cardinality, ValidatorType
from arago.ontology import TurtleEntity as Entity
from arago.ontology import OntologyNamespace as Namespace
from arago.ontology import TurtleVerb as Verb
from arago.ontology import TurtleAttribute as Attribute

# GOAL immutable OGIT model other code can rely on and can't be tinkered with

# TODO __slots__
# TODO test immutability
# TODO validate state
# TODO add static alias Namespace classes


# noinspection SpellCheckingInspection
def namespace_data() -> Generator[Namespace, None, None]:
    # <editor-fold desc="generated namespace data">
    yield Namespace(
        prefix='ogit')
    yield Namespace(
        prefix='ogit.Accounting')
    yield Namespace(
        prefix='ogit.Advertising')
    yield Namespace(
        prefix='ogit.Audit')
    yield Namespace(
        prefix='ogit.Auth')
    yield Namespace(
        prefix='ogit.Auth.Account')
    yield Namespace(
        prefix='ogit.Auth.Application')
    yield Namespace(
        prefix='ogit.Automation')
    yield Namespace(
        prefix='ogit.Cost')
    yield Namespace(
        prefix='ogit.Credit')
    yield Namespace(
        prefix='ogit.CustomerSupport')
    yield Namespace(
        prefix='ogit.Data')
    yield Namespace(
        prefix='ogit.DataProcessing')
    yield Namespace(
        prefix='ogit.Datacenter')
    yield Namespace(
        prefix='ogit.Documents')
    yield Namespace(
        prefix='ogit.Examples')
    yield Namespace(
        prefix='ogit.Examples.Crow')
    yield Namespace(
        prefix='ogit.Factory')
    yield Namespace(
        prefix='ogit.FinancialAccounting')
    yield Namespace(
        prefix='ogit.FinancialAccounting.AccountsPayable')
    yield Namespace(
        prefix='ogit.FinancialMarket')
    yield Namespace(
        prefix='ogit.Forum')
    yield Namespace(
        prefix='ogit.HR')
    yield Namespace(
        prefix='ogit.HR.Recruiting')
    yield Namespace(
        prefix='ogit.Health')
    yield Namespace(
        prefix='ogit.Health.Diagnostics')
    yield Namespace(
        prefix='ogit.Knowledge')
    yield Namespace(
        prefix='ogit.Location')
    yield Namespace(
        prefix='ogit.MARS')
    yield Namespace(
        prefix='ogit.MARS.Application')
    yield Namespace(
        prefix='ogit.MARS.Machine')
    yield Namespace(
        prefix='ogit.MARS.Network')
    yield Namespace(
        prefix='ogit.MARS.Resource')
    yield Namespace(
        prefix='ogit.MARS.Software')
    yield Namespace(
        prefix='ogit.ML')
    yield Namespace(
        prefix='ogit.MRO')
    yield Namespace(
        prefix='ogit.MRO.Aviation')
    yield Namespace(
        prefix='ogit.MRP')
    yield Namespace(
        prefix='ogit.Mobile')
    yield Namespace(
        prefix='ogit.Network')
    yield Namespace(
        prefix='ogit.OSLC-arch')
    yield Namespace(
        prefix='ogit.OSLC-asset')
    yield Namespace(
        prefix='ogit.OSLC-automation')
    yield Namespace(
        prefix='ogit.OSLC-change')
    yield Namespace(
        prefix='ogit.OSLC-core')
    yield Namespace(
        prefix='ogit.OSLC-crtv')
    yield Namespace(
        prefix='ogit.OSLC-ems')
    yield Namespace(
        prefix='ogit.OSLC-perfmon')
    yield Namespace(
        prefix='ogit.OSLC-qm')
    yield Namespace(
        prefix='ogit.OSLC-reqman')
    yield Namespace(
        prefix='ogit.PTF')
    yield Namespace(
        prefix='ogit.Price')
    yield Namespace(
        prefix='ogit.Procurement')
    yield Namespace(
        prefix='ogit.Project')
    yield Namespace(
        prefix='ogit.RDDL')
    yield Namespace(
        prefix='ogit.RL')
    yield Namespace(
        prefix='ogit.RPA')
    yield Namespace(
        prefix='ogit.SaaS')
    yield Namespace(
        prefix='ogit.SalesDistribution')
    yield Namespace(
        prefix='ogit.Schedule')
    yield Namespace(
        prefix='ogit.ServiceManagement')
    yield Namespace(
        prefix='ogit.Software')
    yield Namespace(
        prefix='ogit.Statistics')
    yield Namespace(
        prefix='ogit.Survey')
    yield Namespace(
        prefix='ogit.UserMeta')
    yield Namespace(
        prefix='ogit.Version')
    # </editor-fold>


# verb ogit:any-attributes missing 1 predicate: 'dcterms:valid'
# verb ogit:optional-attributes missing 1 predicate: 'dcterms:valid'
# verb ogit:mandatory-attributes missing 1 predicate: 'dcterms:valid'
# verb ogit:indexed-attributes missing 1 predicate: 'dcterms:valid'
# verb ogit:history missing 1 predicate: 'dcterms:valid'
# verb ogit:allowed missing 1 predicate: 'dcterms:valid'
# verb ogit:from missing 1 predicate: 'dcterms:valid'
# verb ogit:to missing 1 predicate: 'dcterms:valid'

# noinspection SpellCheckingInspection
def verb_data() -> Generator[Verb, None, None]:
    # <editor-fold desc="generated verb data">
    yield Verb(
        about='ogit.Accounting:contributesTo',
        label='contributesTo',
        description='Verb associates which entity contributes to another.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Verb(
        about='ogit.Accounting:has',
        label='has',
        description='Indicates if an entity has another entity.',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Verb(
        about='ogit.Accounting:includes',
        label='includes',
        description='Indicates if an category includes another category.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Verb(
        about='ogit.Accounting:maps',
        label='maps',
        description='Indicates if an category maps another category.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Verb(
        about='ogit.Auth:assigns',
        label='assigns',
        description='Denotes assignments to a RoleAssignment.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Auth:assumes',
        label='assumes',
        description='Denotes membership of an account in a group.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Auth:belongs',
        label='belongs',
        description='Denotes a relationship between two vertices in the Auth domain.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Auth:consents',
        label='consents',
        description='Denotes consent to an Application.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Auth:isMemberOf',
        label='isMemberOf',
        description='Denotes membership of an account in a group.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Auth:uses',
        label='uses',
        description='Denotes use of an Application.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit.Credit:credits',
        label='credits',
        description='This relationship indicates that an entity is the creditor for an instrument.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:debts',
        label='debts',
        description='This relationship indicates that an entity is the debtor for an instrument.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:hasHeadOffice',
        label='hasHeadOffice',
        description='This relationship indicates that an entity has the following head office, i.e. it has the following underlying legal entity.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:hasImmediateParent',
        label='hasImmediateParent',
        description='This relationship indicates that an entity has the following immediate parent, i.e. it is fully, directly controlled by.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:hasUltimateParent',
        label='hasUltimateParent',
        description='This relationship indicates that an entity has the following ultimate parent, i.e. it is fully, directly or indirectly controlled by.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:observes',
        label='observes',
        description='This relationship indicates that an entity observes another entity.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:originates',
        label='originates',
        description='This relationship indicates that an entity originates an instrument to another entity.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:secures',
        label='secures',
        description='This relationship indicates that this entity secures (in the financial sense) another entity.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.Credit:services',
        label='services',
        description='This relationship indicates that an entity services an instrument.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling')
    yield Verb(
        about='ogit.CustomerSupport:collaborates',
        label='collaborates',
        description='a collaborates with many a on b',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Verb(
        about='ogit.CustomerSupport:submits',
        label='submits',
        description='a expects b to receive entity',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Verb(
        about='ogit.Factory:hasAl',
        label='hasAl',
        description='TODO.',
        valid='start=2018-10-19;',
        created_by='arago GmbH')
    yield Verb(
        about='ogit.FinancialMarket:brokers',
        label='brokers',
        description='This relationship indicates that an entity brokers a contract to anothre entity.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit.FinancialMarket:credits',
        label='credits',
        description='This relationship indicates that an entity is the creditor for a contract.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit.FinancialMarket:securedBy',
        label='securedBy',
        description='This relationship indicates that something is secured (in the financial sense) by another entity.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit.FinancialMarket:services',
        label='services',
        description='This relationship indicates that an entity services a contract or instrument.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit.Forum:downloads',
        label='downloads',
        description='This verb represents that a \"User\" has downloaded a given Bundle',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.Forum:features',
        label='features',
        description='This verb represents which KnowledgeBundles are featured (\"choosen\") for a given Group',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.Forum:mentions',
        label='mentions',
        description='This verb was envisaged to represent the *Social Media* menaing of the word mention (or\nthe Twitter-ism *at-mention*). However it simple represents that one entity mentions another,\nfor example cross-references in documentation would also be a valid use-case.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit.Forum:rates',
        label='rates',
        description='This verb represents the `Rating` between two nodes',
        valid='start=2015-08-12;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.HR.Recruiting:appliesFor',
        label='appliesFor',
        description='Indicates if someone applied for something',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel')
    yield Verb(
        about='ogit.HR.Recruiting:recruitsFor',
        label='recruitsFor',
        description='Indicates if someone recruits for something',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel')
    yield Verb(
        about='ogit.HR.Recruiting:submits',
        label='submits',
        description='Indicates if someone submits something',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel')
    yield Verb(
        about='ogit.HR.Recruiting:worksFor',
        label='worksFor',
        description='Indicates if someone works for someone else',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel')
    yield Verb(
        about='ogit.ML:trainedOn',
        label='trainedOn',
        description='it defines model trained on training data.',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit.MRO.Aviation:alternatesWith',
        label='alternatesWith',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:characterize',
        label='characterize',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:conflictsWith',
        label='conflictsWith',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:isPartOf',
        label='isPartOf',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:linksTo',
        label='linksTo',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:orders',
        label='orders',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:overhaul',
        label='overhaul',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:performedAt',
        label='performedAt',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:references',
        label='references',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:suit',
        label='suit',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRO.Aviation:suppliedBy',
        label='suppliedBy',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRP:applies',
        label='applies',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRP:historicised',
        label='historicised',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRP:manufacture',
        label='manufacture',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRP:performs',
        label='performs',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.MRP:supply',
        label='supply',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.OSLC-asset:artifact',
        label='artifact',
        description='The multi valued list of artifacts.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:categorization',
        label='categorization',
        description='A categorization to classify an asset. The category schema values are defined by the service provider. This specification does not define the resource for this property, however it should contain a dcterms:title property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:guid',
        label='guid',
        description='An identifier for the asset. Assigned by the service provider when a resource is created. Different versions of the same asset will share the same identifier.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:model',
        label='model',
        description='The value of the asset model.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:relationshipType',
        label='relationshipType',
        description='The type of this relationship from the perspective of the oslc_asset:relatedAsset resource based on values defined by the service provider. This specification does not define the resource for this property, however it should contain a dcterms:title property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:size',
        label='size',
        description='The size of the artifact media resource in bytes.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:state',
        label='state',
        description='Used to indicate the state of the asset based on values defined by the service provider. This specification does not define the resource for this property, however it should contain a dcterms:title property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:tag',
        label='tag',
        description='Specifies the asset tag value for an Asset. Asset tags are typically human readable labels. For hardware assets, these tags are durable, securely attached to equipment, and may also be readable by barcode and/or RFID.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-asset:version',
        label='version',
        description='The version of the asset. Possible values may include \'1.0\', \'2.0\', etc.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:desiredState',
        label='desiredState',
        description='The intended (domain- or provider-dependant) value of a resource\'s (domain-dependant) \"state\" property after some (future, present or past) process, transition or change. It is expected that this will be a resource reference to a definition of a valid state on the service provider. For example, in the OSLC Automation domain this is used to indicate the desired state of the Automation Request based on values defined in the OSLC Automation specification and, optionally, by the service provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:executesAutomationPlan',
        label='executesAutomationPlan',
        description='Automation Plan run by the Automation Request. It is likely that the target resource will be an oslc_auto:AutomationPlan but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:hasContribution',
        label='contribution',
        description='A result contribution associated with this automation result. It is recommended that the contribution be an inline resource which can be retrieved with the automation result. The recommended attributes beyond the contribution itself are dcterms:title, dcterms:description and dcterms:type to provide a description of the contribution which would be appropriate for display in a simple UI for an automation result.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:inputParameter',
        label='inputParameter',
        description='Parameters provided when Automation Requests are created. These include parameters provided by the creator of the Automation Request (whether by delegated UI or HTTP POST) and *MAY* include additional parameters added by the service provider during Automation Request creation. See the definition of the `oslc_auto:parameterDefinition` attribute of the Automation Plan for additional guidance on determining which parameters are required. Creators of Automation Requests *MAY* provide parameters beyond those defined in the Automation Plan without guarantee the service provider will recognize or honor them. It is expected that this attribute is write-able on Automation Request creation and read-only thereafter.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:outputParameter',
        label='outputParameter',
        description='Automation Result output parameters are parameters associated with the automation execution which produced this Result. This includes the final value of all parameters used to initiate the execution and any additional parameters which may have been created during automation execution by the service provider or external agents. The value of a given `oslc_auto:outputParameter` MAY change as the execution proceeds. Point-in-time accuracy of the values of output parameters is not covered by this specification. Once the Automation Result is in a final state ( `oslc_auto:complete` or `oslc_auto:canceled`), the `oslc_auto:outputParameter` values MUST NOT change.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:parameterDefinition',
        label='parameterDefinition',
        description='The definition of a parameter for this Automation Plan. parameterDefinitions are either a local (inline) or referenced resource and use the attributes (the range) of the oslc:Property resource with one exception. When used in the context of an oslc_auto:parameterDefinition, the cardinality of `oslc:propertyDefinition` becomes zero-or-one instead of exactly-one. Automation consumers creating Automation Requests *MUST* use the `oslc:occurs` attribute of the parameterDefinition, if present, to determine if a given parameter is required when creating the Automation Request. If the `oslc:occurs` attribute indicates the parameter is required (exactly-one or one-or-more), the service provider must guarantee the named parameter will be present in the Automation Result either as an `oslc_auto:inputParameter` when unmodified during execution, or as an `oslc_auto:outputParameter` when modified during execution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:producedByAutomationRequest',
        label='producedByAutomationRequest',
        description='Automation Request which produced the Automation Result. It is likely that the target resource will be an oslc_auto:AutomationResult but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:reportsOnAutomationPlan',
        label='reportsOnAutomationPlan',
        description='Automation Plan which the Automation Result reports on. It is likely that the target resource will be an oslc_auto:AutomationPlan but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:state',
        label='state',
        description='Used to indicate the state of the automation request or result based on values defined in the automation specification and, optionally, by the service provider. Most often a read-only property. It is expected that this will be a resource reference to a definition of a valid automation request or result state on the service provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:usesExecutionEnvironment',
        label='usesExecutionEnvironment',
        description='A resource representing the environment(s) which this Automation Plan can be executed in. The execution environment resource could represent a grouping of environmental details such as operating system, database, browser, compiler, etc.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-automation:verdict',
        label='verdict',
        description='Used to indicate the verdict of the automation result based on values defined by the automation specification and, optionally, by the service provider. Most often a read-only property. It is expected that this will be a resource reference to a definition of a valid automation result verdict on the service provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:affectedByDefect',
        label='affectedByDefect',
        description='Change request is affected by a reported defect. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:affectsTestResult',
        label='affectsTestResult',
        description='Associated QM resource that is affected by this Change Request. It is likely that the target resource will be an oslc_qm:TestResult but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:blocksTestExecutionRecord',
        label='blocksTestExecutionRecord',
        description='Associated QM resource that is blocked by this Change Request. It is likely that the target resource will be an oslc_qm:TestExecutionRecord but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:implementsRequirement',
        label='implementsRequirement',
        description='Implements associated Requirement. It is likely that the target resource will be an oslc_rm:Requirement but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:relatedChangeRequest',
        label='relatedChangeRequest',
        description='This relationship is loosely coupled and has no specific meaning. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:relatedTestCase',
        label='relatedTestCase',
        description='Related QM test case resource. It is likely that the target resource will be an oslc_qm:TestCase but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:relatedTestExecutionRecord',
        label='relatedTestExecutionRecord',
        description='Related to a QM test execution resource. It is likely that the target resource will be an oslc_qm:TestExecutionRecord but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:relatedTestPlan',
        label='relatedTestPlan',
        description='Related QM test plan resource. It is likely that the target resource will be an oslc_qm:TestPlan but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:relatedTestScript',
        label='relatedTestScript',
        description='Related QM test script resource. It is likely that the target resource will be an oslc_qm:TestScript but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-change:testedByTestCase',
        label='testedByTestCase',
        description='Test case by which this change request is tested. It is likely that the target resource will be an oslc_qm:TestCase but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:allowedValues',
        label='allowedValues',
        description='Resource with allowed values for the property being defined. Range of oslc:AllowedValues',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:authorizationURI',
        label='authorizationURI',
        description='URI for obtaining OAuth authorization.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:comment',
        label='comment',
        description='Comment about the resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:creationDialog',
        label='creationDialog',
        description='Enables clients to create a resource via UI.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:creationFactory',
        label='creationFactory',
        description='Enables clients to create new resources.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:describes',
        label='describes',
        description='This shape describes resources that are of the RDF type given by the object of the oslc:describes predicate. Formally, a shape S applies to a resource R if there is a triple R rdf:type T and there is a triple S oslc:describes T.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:details',
        label='details',
        description='A URL that may be used to retrieve a web page to determine additional details about the service provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:discussedBy',
        label='discussedBy',
        description='A series of notes and comments about this resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:domain',
        label='domain',
        description='Namespace URI of the specification that is implemented by this service. In most cases this namespace URI will be for an OSLC domain, but other URIs MAY be used.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:executes',
        label='executes',
        description='Link from a currently available action to the future action it realizes.\n\t\t',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:extendedError',
        label='extendedError',
        description='Extended (additional) error information.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:futureAction',
        label='futureAction',
        description='A predicate that links to an action that is not currently executable on the subject resource,\n\t\tbut may be executable in the future and/or on other resources.\n\t\tFor example, in OSLC Automation this is expected to link from an oslc_auto:AutomationPlan to an\n\t\toslc:Action resource with zero bindings (as it is not executable),\n\t\twith the meaning that the executable form of the action may be available on oslc_auto:AutomationResult resources\n\t\tgenerated by executing that Automation Plan.  Similarly, resource shapes can allow discovery of actions\n\t\tavailable on the output of a creation factory.\n\t\t',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:inReplyTo',
        label='inReplyTo',
        description='Reference to comment this comment is in reply to.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:instanceShape',
        label='instanceShape',
        description='The URI of a Resource Shape that describes the possible properties.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:modifiedBy',
        label='modifiedBy',
        description='The URI of a resource describing the entity that most recently modified this resource.  The link target is usually a foaf:Person or foaf:Agent, but could be any type.  This is modeled after dcterms:creator, but Dublin Core currently has no equivalent property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:moreInfo',
        label='moreInfo',
        description='A resource giving more information on the error SHOULD be of an HTML content-type.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:nextPage',
        label='nextPage',
        description='Link to next page of response.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:oauthAccessTokenURI',
        label='oauthAccessTokenURI',
        description='URI for obtaining OAuth access token.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:oauthConfiguration',
        label='oauthConfiguration',
        description='Defines the three OAuth URIs required for a client to act as an OAuth consumer.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:oauthRequestTokenURI',
        label='oauthRequestTokenURI',
        description='URI for obtaining OAuth request token.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:occurs',
        label='occurs',
        description='MUST be either http://open-services.net/ns/core#Exactly-one, http://open-services.net/ns/core#Zero-or-one, http://open-services.net/ns/core#Zero-or-many or http://open-services.net/ns/core#One-or-many.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:partOfDiscussion',
        label='partOfDiscussion',
        description='Reference to owning Discussion resource .',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:property',
        label='property',
        description='The properties that are allowed or required by this shape.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:propertyDefinition',
        label='propertyDefinition',
        description='URI of the property whose usage is being described.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:queryBase',
        label='queryBase',
        description='The base URI to use for queries. Queries may be invoked either by HTTP GET or HTTP POST. For HTTP GET, a query URI is formed by appending a key=value pair to the base URI. For HTTP POST, the query parameters are encoded as content with media type application/x-www-form-urlencoded and sent in the request body. The base URI MAY accept other query languages and media types in the request body, e.g. application/sparql-query for SPARQL queries.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:queryCapability',
        label='queryCapability',
        description='Enables clients query across a collection of resources.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:range',
        label='range',
        description='For properties with a resource value-type, Providers MAY also specify the range of possible resource types allowed, each specified by URI. The default range is http://open-services.net/ns/core#Any.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:resourceShape',
        label='resourceShape',
        description='A Creation Factory MAY provide Resource Shapes that describe shapes of resources that may be created.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:resourceType',
        label='resourceType',
        description='The expected resource type URI of the resource that will be created using this creation factory. These would be the URIs found in the result resource\'s rdf:type property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:results',
        label='results',
        description='Used to hold the results of dialog action or JSON query results (default).\n\t\tThe JSON query result attribute \'oslc:results\' is used whenever a provider doesn\'t have\n\t\ta suitable property already in its model for such purposes.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:selectionDialog',
        label='selectionDialog',
        description='Enables clients to select a resource via UI.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:service',
        label='service',
        description='Describes a service offered by the service provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:serviceProviderCatalog',
        label='serviceProviderCatalog',
        description='Additional service provider catalog.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:valueShape',
        label='valueShape',
        description='if the value-type is a resource type, then Property MAY provide a shape value to indicate the Resource Shape that applies to the resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-core:valueType',
        label='valueType',
        description='A URI that indicates the value type, for example XML Schema or RDF URIs for literal value types, and OSLC-specified for others.  If this property is omitted, then the value type is unconstrained.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:assetTag',
        label='assetTag',
        description='Specifies the asset tag for a physical piece of equipment. Asset tags are typically human readable labels that are durable and securely attached to equipment. Asset tags may also be readable by barcode and/or RFID. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:dbInstance',
        label='dbInstance',
        description='The Software Server representing the database instance that manages this database.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:dependsOn',
        label='dependsOn',
        description='A relationship denoting that the source of the relationship cannot function properly without an association with the target. The dependency is directional ( the source depends on the target but the reverse is not necessarily true ) and can represent any cause or type of dependency. For instance, this relationship can be used to denote that a device depends on its power supply(s) or that an IP path depends on a layer 2 connection.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:deployedTo',
        label='deployedTo',
        description='The SoftwareServer on which this SoftwareModule is deployed.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:elementFrom',
        label='elementFrom',
        description='The resource acting as the origination point in the ordered path.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:elementTo',
        label='elementTo',
        description='The resource acting as the destination point in the ordered path.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:parentServiceInstance',
        label='parentServiceInstance',
        description='When context is required, this is the containing Application for the set of Transactions. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:runsOn',
        label='runsOn',
        description='The ComputerSystem this SoftwareServer instance is running on.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-crtv:serverAccessPoint',
        label='serverAccessPoint',
        description='The Server Access Point clients use for communications with this resource. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:assumes',
        label='assumes',
        description='\nThis property links a scenario to the assumed value for some measure, e.g. duration, size.\nThe assumed value is a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:assumesTable',
        label='assumesTable',
        description='\nThis property links a scenario to the assumed value for some fact table of measures, e.g. staffing by week.\nThe assumed fact table contains probability distributions.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:assumesWbs',
        label='assumesWbs',
        description='\nThis property links a scenario to the assumed work breakdown structure.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:baselineList',
        label='baselineList',
        description='This property links a service to its baseline list.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:cdfPoint',
        label='cdfPoint',
        description='\nThis property links a cumulative probability function resource to one or more points on its graph.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:currentBaseline',
        label='currentBaseline',
        description='This property links a project to its current baseline.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:dimension',
        label='dimension',
        description='\nThis property links a resource to a dimension.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:dimensionCell',
        label='dimensionCell',
        description='\nThis property links a fact row to one or more of its dimension cells.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:dimensionColumn',
        label='dimensionColumn',
        description='\nThis property links the head of a fact table to one or more\n<a href=\"#DimensionColumn\"><code>ems:DimensionColumn</code></a>\nresources that define dimension columns.\nEvery fact table MUST have at least one dimension column.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:dimensionMember',
        label='dimensionMember',
        description='\nThis property links a dimension cell to its dimension member.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:distribution',
        label='distribution',
        description='\nThis property links a resource, e.g. <a href=\"#MeasureDistribution\">ems:MeasureDistribution</a>\nto a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:estimate',
        label='estimate',
        description='The property links a resource to an estimate.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:estimateList',
        label='estimateList',
        description='This property links a service to its estimate list.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:extendsScenario',
        label='extendsScenario',
        description='\nThis property links a scenario a base scenario that it extends.\nThe base scenario contains assumptions that can be included in several other extended scenarios.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:fact',
        label='fact',
        description='\nThis property links a fact table to its fact rows.\nIn general, a fact table will have many fact rows.\nIf the fact table has an\n<a href=\"#tableSource\"><code>ems:tableSource</code></a> property,\nthen the rows of the fact table MUST be a copy of the data values received in the response of\nan HTTP GET request of the URL of the remote table source.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:grain',
        label='grain',
        description='\nThis property links a resource to a grain.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:head',
        label='head',
        description='\nThis property links a fact table to an\n<a href=\"#Head\"><code>ems:Head</code></a> resource that\ndescribes the columns of the table.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:inColumn',
        label='inColumn',
        description='\nThis property links a cell to its column.\nDimension cells\n(see <a href=\"#DimensionCell\"><code>ems:DimensionCell</code></a>)\nare linked to dimension columns\n(see <a href=\"#DimensionColumn\"><code>ems:DimensionColumn</code></a>).\nMeasure cells\n(see <a href=\"#MeasureCell\"><code>ems:MeasureCell</code></a>)\nare linked to measure columns\n(see <a href=\"#MeasureColumn\"><code>ems:MeasureColumn</code></a>).',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:map',
        label='map',
        description='\nThis property links a fact table head to an\n<a href=\"#Map\"><code>ems:Map</code></a> resource that defines\nhow custom dimension values are mapped to standard values.\nThe scope of this mapping is local to the fact table.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:mapping',
        label='mapping',
        description='\nThis property links a map to a mapping.\nA map may have one or more mappings.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:measureCell',
        label='measureCell',
        description='\nThis property links a fact row to one or more of its measure cells.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:measureColumn',
        label='measureColumn',
        description='\nThis property links the head of a fact table to one or more\n<a href=\"#MeasureColumn\"><code>ems:MeasureColumn</code></a> resources that define measure columns.\nEvery fact table MUST have at least one measure column.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:measureDistributionCell',
        label='measureDistributionCell',
        description='\nThis property links a fact distribution row to a measure distribution cell.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:measurementList',
        label='measurementList',
        description='This property links a service to its measurement list.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:memberBaseline',
        label='memberBaseline',
        description='This property links a baseline list to its member baselines.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:memberEstimate',
        label='memberEstimate',
        description='This property links an estimate list to its member estimates.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:memberMeasurement',
        label='memberMeasurement',
        description='This property links a measurement list to its member measurements.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:memberProject',
        label='memberProject',
        description='This property links a project list to its member projects.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:memberScenario',
        label='memberScenario',
        description='This property links a scenario list to its member scenarios.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:metric',
        label='metric',
        description='\nThis property links a measure to its metric.\nFor example, the measure <em>duration of 12 months</em> has the metric <em>duration</em>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:observes',
        label='observes',
        description='\nThis property links a measurement to the observed value of a measure.\nIn an EMS service, the measurement is a resource of type\n<a href=\"#Measurement\"><code>ems:Measurement</code></a>\nwhich may observe zero or more measures.\nFor example, a measurement at the end of a project may observe a <em>duration of 12 months</em> and a <em>cost of 200,000 USD</em>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:observesTable',
        label='observesTable',
        description='\nThis property links a measurement to the observed fact table.\nThe fact table analyzes the measurement along one or more dimensions.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:observesWbs',
        label='observesWbs',
        description='\nThis property links a measurement to the observed work breakdown structure.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:predicts',
        label='predicts',
        description='\nThis property links an estimate to the predicted value for some measure, e.g. duration, size.\nThe predicted value is a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:predictsTable',
        label='predictsTable',
        description='\nThis property links an estimate to the predicted value for some fact table of measures, e.g. staffing by week.\nThe predicted fact table contains probability distributions.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:predictsWbs',
        label='predictsWbs',
        description='\nThis property links an estimate to the predicted work breakdown structure.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:project',
        label='project',
        description='The property links a resource to a project.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:projectList',
        label='projectList',
        description='This property links a service to its project list.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:quantile',
        label='quantile',
        description='\nThis property links a quantile function resource to one or more quantiles.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:scenarioList',
        label='scenarioList',
        description='This property links a service to its scenario list.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:seeAlsoEstimation',
        label='seeAlsoEstimation',
        description='This property links a project to a corresponding resource in an estimation application.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:seeAlsoPerformance',
        label='seeAlsoPerformance',
        description='This property links a project to a corresponding resource in a performance management application.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:seeAlsoPortfolio',
        label='seeAlsoPortfolio',
        description='This property links a project to a corresponding resource in a portfolio management application.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:seeAlsoProject',
        label='seeAlsoProject',
        description='This property links a project to a corresponding resource in a project management application.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:service',
        label='service',
        description='\nThis property is used to link a resource to the EMS service instance that hosts it.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:tableSource',
        label='tableSource',
        description='\n<p>Fact tables contain actual measurements for projects, systems, or things.\nIn practice, there may be many measurements and they may be updated frequently.\nThe measurements may be at a finer level of granularity than the estimates,\ne.g. a project may estimate total defects found per month,\nwhereas the actual number found may be collected daily.\nFurthermore, these measurements are often collected automatically by software development tools\nsuch as bug tracking systems or source code control systems.\nIt may therefore be useful to simply refer to the source of the measurements rather than copy\nthe actual measurements into the EMS service provider,\ne.g. a dynamic query on a software tool may generate the fact table on demand.</p>\n\n<p>This property lets you refer to the remote source of the fact table data via a URL.\nAn HTTP GET request on this URL MUST return an\n<a href=\"#FactTable\"><code>ems:FactTable</code></a> resource whose\n<code>dcterms:title</code> and\n<a href=\"#head\"><code>ems:head</code></a> properties match this resource.</p>',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:to',
        label='to',
        description='\nThis property links a mapping to its dimension member URI.\nMany mappings MAY map to the same dimension member URI.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:unitOfMeasure',
        label='unitOfMeasure',
        description='\nThis property gives the unit of measure. For example, the measure <em>duration of 12 months</em> has a unit of measure <em>months</em>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:useMap',
        label='useMap',
        description='\nThis property links a resource to a map.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:wbsContent',
        label='wbsContent',
        description='\nThis property gives the literal XML WBS content of a WBS resource.\nThis content MUST be in the XML format specified by the WBS resource.\nIf this property is absent, then <code>ems:wbsSource</code> MUST be present.\nIf this property and <code>ems:wbsSource</code> are present,\nthen the value of this property SHOULD be the XML document representation returned in the\nHTTP GET response for the link given in <code>ems:wbsSource</code>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:wbsFormat',
        label='wbsFormat',
        description='\nThis property links a WBS resource to the XML format of its content.\nEMS does not define a format for WBS content.\nInstead, this property identifies the specification that defines the XML format of the WBS content.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-ems:wbsSource',
        label='wbsSource',
        description='\nThis property links a WBS resource to a resource that contains the WBS XML content.\nThis content MUST be in the XML format specified by the WBS resource.\nWhen this link is deferenced using an HTTP GET request, the response MUST be the WBS.\nIf this property is absent, then the WBS resource MUST have a\n<a href=\"#wbsContent\"><code>ems:wbsContent</code></a> property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-perfmon:process',
        label='process',
        description='A process running, for example, in a computer system. Typically refers to a resource with type crtv:ComputerSystem, but it may refer to other resource types.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:affectedByChangeRequest',
        label='affectedByChangeRequest',
        description='Change request that affects the Test Result. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:blockedByChangeRequest',
        label='blockedByChangeRequest',
        description='Change Request that prevents execution of the Test Execution Record. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:executesTestScript',
        label='executesTestScript',
        description='Test Script executed to produce the Test Result. It is likely that the target resource will be an oslc_qm:TestScript but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:executionInstructions',
        label='executionInstructions',
        description='Instructions for executing the test script. Note that the value of Occurs is undefined. The resource shape document provided by the QM service provider may be consulted for its value.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:producedByTestExecutionRecord',
        label='producedByTestExecutionRecord',
        description='Test Execution Record that the Test Result was produced by. It is likely that the target resource will be an oslc_qm:TestExecutionRecord but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:relatedChangeRequest',
        label='relatedChangeRequest',
        description='A related change request. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:reportsOnTestCase',
        label='reportsOnTestCase',
        description='Test Case that the Test Result reports on. It is likely that the target resource will be an oslc_qm:TestCase but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:reportsOnTestPlan',
        label='reportsOnTestPlan',
        description='Test Plan that the Test Execution Record reports on. It is likely that the target resource will be an oslc_qm:TestPlan but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:runsOnTestEnvironment',
        label='runsOnTestEnvironment',
        description='Indicates the environment details of the test case for this execution record.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:runsTestCase',
        label='runsTestCase',
        description='Test Case run by the Test Execution Record. It is likely that the target resource will be an oslc_qm:TestCase but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:testsChangeRequest',
        label='testsChangeRequest',
        description='Change Request tested by the Test Case. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:usesTestCase',
        label='usesTestCase',
        description='Test Case used by the Test Plan. It is likely that the target resource will be an oslc_qm:TestCase but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:usesTestScript',
        label='usesTestScript',
        description='Test Script used by the Test Case. It is likely that the target resource will be an oslc_qm:TestScript but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:validatesRequirement',
        label='validatesRequirement',
        description='Requirement that is validated by the Test Case. It is likely that the target resource will be an oslc_rm:Requirement but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-qm:validatesRequirementCollection',
        label='validatesRequirementCollection',
        description='Requirement Collection that is validated by the Test Plan. It is likely that the target resource will be an oslc_rm:RequirementCollection but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:affectedBy',
        label='affectedBy',
        description='Expresses an affects relationship\n            between entities. For example, a defect may be said to affect a\n            requirement.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:elaboratedBy',
        label='elaboratedBy',
        description='Expresses an elaboration relationship\n            between entities. For example, a model element can elaborate a\n            requirement.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:implementedBy',
        label='implementedBy',
        description='Expresses an implementation\n            relationship between entities.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:specifiedBy',
        label='specifiedBy',
        description='Expresses a specification relationship\n            between entities. For example, a model element can specifiy a\n            requirement.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:trackedBy',
        label='trackedBy',
        description='Expresses a tracking relationship\n            between entities. For example, a change request may be said to track a\n            requirement, in that it governs the changes to a requirement according to some\n            process machinery.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:uses',
        label='uses',
        description='Expresses a use relationship between\n            entities. For example, a requirement collection may use a\n            requirement.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.OSLC-reqman:validatedBy',
        label='validatedBy',
        description='Expresses a validation relationship\n            between entities. For example, a test plan may be said to validated a requirement\n            collection.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.RDDL:nature',
        label='nature',
        description='A machine-readable label provided by the value of the xlink:role attribute',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.RDDL:resource',
        label='resource',
        description='This property is used to specify a resource relationship',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit.RPA:Operates',
        label='Operates',
        description='entity operates on in aonther entity. Robot operates in Robotic environment.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit.UserMeta:asks',
        label='asks',
        description='This verb represents that a games asks a question',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.UserMeta:loses',
        label='loses',
        description='This verb represents that a user has lost a game',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.UserMeta:plays',
        label='plays',
        description='This verb represents that a user has played a game',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit.UserMeta:wins',
        label='wins',
        description='This verb represents that a user has won a game',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit:Verb',
        label='Verb',
        description='Represents the class of all Verbs',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Verb(
        about='ogit:accepts',
        label='accepts',
        description='Indicates if an entity accepts something else.',
        valid='start=2015-09-02;',
        created_by='bmoore@arago.de')
    yield Verb(
        about='ogit:activates',
        label='activates',
        description='entity activates other entity.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit:affects',
        label='affects',
        description='The relationship indicates that one entity affects some other entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:alerts',
        label='alerts',
        description='Verb showing if one entity alerts another.',
        valid='start=2016-10-26;',
        created_by='stravlos@arago.co')
    yield Verb(
        about='ogit:allowed',
        label='allowed',
        description='Constrains ranges and domains for Verbs')
    yield Verb(
        about='ogit:any-attributes',
        label='any-attributes',
        description='The list of any Attributes for an Entity')
    yield Verb(
        about='ogit:approves',
        label='approves',
        description='Indicates if an entity approves something else.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:assignedTo',
        label='assignedTo',
        description='Verb expressing which entity could be assigned to which another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:associates',
        label='associates',
        description='Verb indicating if an entity associates with another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:assumes',
        label='assumes',
        description='verb which allows to connect the planning parameters to a planning template',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:availableIn',
        label='availableIn',
        description='Indicates that something can be found from somewhere.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:belongs',
        label='belongs',
        description='Verb showing if one entity belongs to another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:bills',
        label='bills',
        description='Indicates if one entity bills another one, e.g. an Invoice bills an Order',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:calls',
        label='calls',
        description='Verb showing which entity calls which another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:causes',
        label='causes',
        description='Indicates that one entity causes the creation of another one.\nE.g. an error situation during change execution might lead to a new incident ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:closes',
        label='closes',
        description='Indicates if one entity closes another one, e.g. a Person might close a Ticket',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:communicatesWith',
        label='communicatesWith',
        description='indicates which entities can communicate with other entities',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:competes',
        label='competes',
        description='This relationship defines that one entity competes another entity.',
        valid='start=2015-09-18;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:complies',
        label='complies',
        description='Indicates wether one entity should comply to another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:concludes',
        label='concludes',
        description='Verb showing if a legal entity concludes something (e.g. Contract).',
        valid='start=2015-06-18;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:configures',
        label='configures',
        description='The `from` entity, contains configuration data for the to `entity`',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit:conformsTo',
        label='conformsTo',
        description='allows reference to a Schema',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:connects',
        label='connects',
        description='Verb showing that an entity is physically/virtually connecting to another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:consistsOf',
        label='consistsOf',
        description='It shows, that the destination entity is a non-exclusive part of the source.',
        valid='start=2018-02-13;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:consumes',
        label='consumes',
        description='This relationship indicates that one consumes result of work from another.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Verb(
        about='ogit:contains',
        label='contains',
        description='This relationship indicates that something is part of something else. see also \"includes\"',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:contributes',
        label='contributes',
        description='Verb associates which entity contributes to another, for example could be used to express a distribution for the percentage \nof a cost element, which contributes to another cost element.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:corresponds',
        label='corresponds',
        description='Indicates wether one entity could correpond to a more general one, e.g. an Incident could correspond to a Ticket',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:covers',
        label='covers',
        description='Verb showing which entity covers another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:creates',
        label='creates',
        description='Indicates if one entity creates another one.',
        valid='start=2015-05-19;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:defines',
        label='defines',
        description='General relationship indicating that some entitiy defines some other.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:deliversTo',
        label='deliversTo',
        description='This relationship defines that one entity delivers sth. to another entity.',
        valid='start=2015-10-22;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:demands',
        label='demands',
        description='Verb indicating if an entity demands another entity.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Verb(
        about='ogit:dependsOn',
        label='dependsOn',
        description='This relationship indicates that some entity is depending on some other. E.g. machine hosts software.',
        valid='start=2015-10-15;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:deployedTo',
        label='deployedTo',
        description='Verb associates if something was deployed to another entity/component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:derivesFrom',
        label='derivesFrom',
        description='The derivesFrom of a version. This verb could be generated internally.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de')
    yield Verb(
        about='ogit:describes',
        label='describes',
        description='This relationship allows to associate additional information with an entity. The \"described\" node can have many \"describing\" nodes.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:desires',
        label='desires',
        description='It is not required. But strong wish to have something or wish for something to happen.',
        valid='start=2019-03-28;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit:dislikes',
        label='dislikes',
        description='Indicates if an entity (mostly Person) dislikes something else.',
        valid='start=2015-09-15;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:employs',
        label='employs',
        description='Verb indicating if one entity employes another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:endorses',
        label='endorses',
        description='This relationship indicates that one entity endorses some other. This is a recommendation or a\nsocial `like`.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit:extends',
        label='extends',
        description='Indicates if one entity extends another one',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:follows',
        label='follows',
        description='Indicates if one entity follows another, as in a sequence flow  connecting two elements of a process.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:forks',
        label='forks',
        description='General relationship indicating that some entitiy forks some other, assuming the same type.',
        created_at='2018-06-12',
        modified_at='2018-06-12',
        valid='start=2018-06-12;',
        created_by='Vitaly Teremasov',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Verb(
        about='ogit:from',
        label='from',
        description='Constrains domains for Verbs')
    yield Verb(
        about='ogit:generates',
        label='generates',
        description='Verb indicating if an entity generates another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:governs',
        label='governs',
        description='Verb showing if an entity governs/enforces another one.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:has',
        label='has',
        description='Indicates if an entity has another entity.',
        valid='start=2019-03-28;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit:hiddenBy',
        label='hiddenBy',
        description='An entity has been hidden by another Entity.',
        valid='start=2017-07-04;',
        created_by='Kristjan Liiva')
    yield Verb(
        about='ogit:history',
        label='history',
        description='This represents the change history of an Entity, Attribute or Verb')
    yield Verb(
        about='ogit:hosts',
        label='hosts',
        description='verb which shows that an entity is hosted in another entity.',
        valid='start=2015-10-15;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:ignores',
        label='ignores',
        description='Verb showing that one entity ignores another - (useful as a mark-as-read flag)',
        valid='start=2016-10-14;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit:implements',
        label='implements',
        description='Defines that an entity provides the implementation for another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:includes',
        label='includes',
        description='Indicates if an entity includes something else.',
        valid='start=2018-07-05;',
        created_by='qikram@arago.de')
    yield Verb(
        about='ogit:index',
        label='index',
        description='Indicates if one entity have indexed attributes (only use within ontology itself).',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Verb(
        about='ogit:indexed-attributes',
        label='indexed-attributes',
        description='The list of indexed Attributes for an Entity')
    yield Verb(
        about='ogit:installs',
        label='installs',
        description='Indicates which entities are installed by other entities.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:invites',
        label='invites',
        description='Indicates if an entity (mostly Person) invites something else.',
        valid='start=2015-09-15;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:isPartOf',
        label='isPartOf',
        description='Indicates if an entity is part of another entity.',
        valid='start=2019-03-22;',
        created_by='Kaushik Gondaliya')
    yield Verb(
        about='ogit:issues',
        label='issues',
        description='This verb means that one entity creates or hands out another entity.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:leads',
        label='leads',
        description='This relationship defines that one entity leads another entity.',
        valid='start=2015-10-22;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:likes',
        label='likes',
        description='Indicates if an entity (mostly Person) likes something else.',
        valid='start=2015-09-15;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:listedAt',
        label='listedAt',
        description='Verb showing that one entity is listed at another entity.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:locatedAt',
        label='locatedAt',
        description='Indicates that an entity is located at another entity.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:locatedIn',
        label='locatedIn',
        description='indicate that something has its place somewhere',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:manages',
        label='manages',
        description='This relationship indicates that one entity manages some other.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:mandatory-attributes',
        label='mandatory-attributes',
        description='The list of mandatory Attributes for an Entity')
    yield Verb(
        about='ogit:moderates',
        label='moderates',
        description='Moderation as a verb, in the context of a forum, is a supervisory role. It implies that the\nentity takes a responsibility for the maintenance and upkeep of the connected entity.',
        valid='start=2015-04-23;',
        created_by='cwalker@arago.de',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit:opens',
        label='opens',
        description='Indicates an entity which creates/opens another entity (e.g. Person opens Ticket).',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:optional-attributes',
        label='optional-attributes',
        description='The list of optional Attributes for an Entity')
    yield Verb(
        about='ogit:opts',
        label='opts',
        description='Indicates if one entity opts having a second one (non mandatory dependency)',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Verb(
        about='ogit:organizes',
        label='organizes',
        description='Indicates that an entity organizes another entity.',
        valid='start=2020-09-28;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:owns',
        label='owns',
        description='This relationship indicates that one entity owns some other.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:performs',
        label='performs',
        description='TODO.',
        valid='start=2016-02-25;',
        created_by='bneal@arago.de')
    yield Verb(
        about='ogit:plans',
        label='plans',
        description='Verb showing how one entity plans/predicts on the content of another entity',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:precedes',
        label='precedes',
        description='Describes the relation between a predecessor and a successor entity. This can be use in two ways:\nEither do define some temporal order of things. Or to define some dependency of actions to be done.\nThe application managing such dependency graphs is responsible to prevent cyclic dependencies.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:prioritizes',
        label='prioritizes',
        description='Indicates if an entity set priority for something else.',
        valid='start=2015-09-02;',
        created_by='bmoore@arago.de')
    yield Verb(
        about='ogit:produces',
        label='produces',
        description='This relationship indicates that one produces some work for another.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Verb(
        about='ogit:proves',
        label='proves',
        description='One entity can \"prove\" another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:provides',
        label='provides',
        description='Verb showing if one entity provides something to another.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:rates',
        label='rates',
        description='This verb represents the `Rating` between two nodes',
        valid='start=2018-08-01;',
        created_by='qikram@arago.de')
    yield Verb(
        about='ogit:readBy',
        label='readBy',
        description='An entity has been read by another Entity.',
        valid='start=2017-07-04;',
        created_by='Kristjan Liiva')
    yield Verb(
        about='ogit:receives',
        label='receives',
        description='an entity receives something another entity',
        valid='start=2017-02-17;',
        created_by='stravlos@arago.de')
    yield Verb(
        about='ogit:receivesFrom',
        label='receivesFrom',
        description='an entity receives data from another entity',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:references',
        label='references',
        description='Verb indicating if an entity references another entity.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:registeredAt',
        label='registeredAt',
        description='Indicates that an entity is registered at another entity.',
        valid='start=2020-09-28;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:rejects',
        label='rejects',
        description='Indicates if an entity rejects something else.',
        valid='start=2015-09-02;',
        created_by='bmoore@arago.de')
    yield Verb(
        about='ogit:relates',
        label='relates',
        description='General relationship indicating that one entity is related to another one.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:repliedWith',
        label='repliedWith',
        description='This relationship indicates that user replied with something.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Verb(
        about='ogit:reportedOn',
        label='reportedOn',
        description='Indicates where a failure situation was initially observed. In case an incident record is created from an event management system this relationship points to the entitiy that represents the monitored device/endpoint.\nWe call it \"reportedOn\" instead of \"observedOn\" to account for the close relation to \"reportedAt\", \"reportedBy\"',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:reports',
        label='reports',
        description='Verb showing which entity reports to which another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:represents',
        label='represents',
        description='This relationship defines that one entity represents another entity.',
        valid='start=2017-04-11;',
        created_by='arago GmbH')
    yield Verb(
        about='ogit:requests',
        label='requests',
        description='Indicates if one entity requests another, e.g. Person requests a ChangeRequest. This might be different from the person \nwho created the ticket (ogit/ITSM/opendBy) in case the reporter is calling a service desk and the ticket will be opened \nby help desk staff. Sometimes also named as \"caller\". This Person or entity must be kept informed about relevant updates \nof the ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:requires',
        label='requires',
        description='Indicates dependencies between entities in the sense of \"necessary condition\".',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:responds',
        label='responds',
        description='This relationship indicates that one entity is a response to another. For example, parts of a\nconversation/fourm thread.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit:reviews',
        label='reviews',
        description='One entity reviews another',
        valid='start=2018-07-13;',
        created_by='Mikhail Osher')
    yield Verb(
        about='ogit:runsOn',
        label='runsOn',
        description='Shows if a certain component is running on another component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:seenBy',
        label='seenBy',
        description='An entity has been seen by another Entity.',
        valid='start=2017-07-04;',
        created_by='Kristjan Liiva')
    yield Verb(
        about='ogit:sells',
        label='sells',
        description='This relationship defines that one entity sells another entity.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:sellsTo',
        label='sellsTo',
        description='This relationship defines that one entity sells sth. to another entity.',
        valid='start=2015-10-22;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:sends',
        label='sends',
        description='an entity sends data to another entity',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:soldTo',
        label='soldTo',
        description='This relationship indicates that something is sold to another entity.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Verb(
        about='ogit:solves',
        label='solves',
        description='One entity can \"solve\" another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:specifies',
        label='specifies',
        description='One entity \"specifies\" another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:subscribes',
        label='subscribes',
        description='A subscription by an entity to another. Implies that one entity is interested in something\nthe other can offer.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de')
    yield Verb(
        about='ogit:supervises',
        label='supervises',
        description='Indicates if an entity supervises another entity. E.g. a Person supervises a Ticket or a Task.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:supports',
        label='supports',
        description='This relationship defines that one entity provides/supports another entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:to',
        label='to',
        description='Constrains ranges for Verbs')
    yield Verb(
        about='ogit:tracks',
        label='tracks',
        description='This relationship defines that one entity tracks another entity.',
        valid='start=2017-06-26;',
        created_by='vteremasov@klika-tech.com')
    yield Verb(
        about='ogit:transfers',
        label='transfers',
        description='Indicates if one entity transfers information to another.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:triggers',
        label='triggers',
        description='This relationship indicates that one entity triggers some other.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:updates',
        label='updates',
        description='Indicates which entity (e.g. Person) updated each another entity (e.g. Ticket).',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:uses',
        label='uses',
        description='This relationship indicates that some entity is used by some other.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:utilizes',
        label='utilizes',
        description='This verb means a effective usage of something, for example a component.',
        valid='start=2018-02-08;',
        created_by='Viktor Voss')
    yield Verb(
        about='ogit:validFor',
        label='validFor',
        description='This relationship indicates the something specifies validity for something else.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Verb(
        about='ogit:versions',
        label='versions',
        description='The version of a node. This verb is generated internally.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de')
    yield Verb(
        about='ogit:virtualizes',
        label='virtualizes',
        description='Shows if an entity or a component virtualizes another entity or component .',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Verb(
        about='ogit:wins',
        label='wins',
        description='Associates the entity that has won something with the thing that was won. Despite the present\ntense used in the verb, this almost always will refer to some that *was* won in the past.',
        valid='start=2015-04-23;',
        created_by='cwalker@arago.de',
        cardinality=Cardinality.MANY_TO_MANY)
    yield Verb(
        about='ogit:worksOn',
        label='worksOn',
        description='Indicates if one entity is currently working on another entity.',
        valid='start=2015-06-24;',
        created_by='Peter Larem')
    # </editor-fold>


# attribute ogit:cardinality missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:deleter missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:hide missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:parent missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:scope missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:admin-contact missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:tech-contact missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:validation-type missing 2 predicates: 'dcterms:description', 'dcterms:valid'
# attribute ogit:validation-parameter missing 2 predicates: 'dcterms:description', 'dcterms:valid'

# noinspection SpellCheckingInspection
def attribute_data() -> Generator[Attribute, None, None]:
    # <editor-fold desc="generated attribute data">
    yield Attribute(
        about='ogit.Accounting:AccountNumber',
        label='AccountNumber',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:NAOCategorizations',
        label='NAOCategorizations',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:TrialBalanceTargetAccountByNumber',
        label='TrialBalanceTargetAccountByNumber',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:accountingStandard',
        label='accountingStandard',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:association',
        label='association',
        description='A association to one ore more standard categories',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:balance',
        label='balance',
        description='For a period, or for a category aggregated balance in the related currency',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:detailedCategories',
        label='detailedCategories',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:mainCategories',
        label='mainCategories',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:periods',
        label='periods',
        description='Aone ore more periods of a financial statement.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:primaryReportingPeriod',
        label='primaryReportingPeriod',
        description='Unknown',
        valid='start=2018-12-12;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:rank',
        label='rank',
        description='A rank of the item in a financial statement.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:subtype',
        label='subtype',
        description='A subtype of a financial statement. Possible values are: Trial Balance, Balance Sheet, Net Accet Overview',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit.Accounting:template',
        label='template',
        description='A template of a financial statement.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit:Attribute',
        label='Attribute',
        description='Represents the class of all Attributes',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Auth.Account:acceptedEmails',
        label='acceptedEmails',
        description='Flag about whether emails were accepted',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:acceptedPrivacy',
        label='acceptedPrivacy',
        description='Flag about whether privacy terms were accepted',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:acceptedProjectTerms',
        label='acceptedProjectTerms',
        description='Flag about whether HIRO Project terms were accepted',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:acceptedTerms',
        label='acceptedTerms',
        description='Flag about whether usage terms were accepted',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:allowCookies',
        label='allowCookies',
        description='Flag about whether cookies are allowed',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:defaultScope',
        label='defaultScope',
        description='Default working data scope of an account',
        created_at='2019-12-01',
        modified_at='2019-12-01',
        valid='start=2019-12-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:defaultTeam',
        label='defaultTeam',
        description='Default team of an ogit/Auth/Account',
        created_at='2020-01-01',
        modified_at='2020-01-01',
        valid='start=2020-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:displayName',
        label='displayName',
        description='Display name of an account',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Account:statusReason',
        label='statusReason',
        description='Status Reason of an ogit/Auth/Account',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        validation_type=ValidatorType.FIXED,
        validation_parameter='UserDeactivated,AdminDeactivated,PasswordExpired,AutoDeactivated')
    yield Attribute(
        about='ogit.Auth.Account:type',
        label='type',
        description='Type of an account. Values: person, application',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Application:parent',
        label='parent',
        description='Parent of an application',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Application:status',
        label='status',
        description='Status of an application',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Application:type',
        label='type',
        description='Type of an application',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth.Application:urls',
        label='urls',
        description='URL of an application',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth:_iam-domain',
        label='_iam-domain',
        description='IAM Domain of an entity',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth:allowedTypes',
        label='allowedTypes',
        description='Allowed types for authorization',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth:edgeRule',
        label='edgeRule',
        description='Contains jfilter expression for the allowed edge operations',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth:restricted',
        label='restricted',
        description='Contains flag about whether Auth/DataSet is restricted',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Auth:vertexRule',
        label='vertexRule',
        description='Contains jfilter expression for the allowed vertex operations',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit.Automation:additionalMacAddress',
        label='additionalMacAddress',
        description='Contains an additional MAC address',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:adminUrl',
        label='adminUrl',
        description='Contains an URL (unified resource locator)',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:affectedNodeId',
        label='affectedNodeId',
        description='Contains the ID of the node which is affected by this entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:appInfrastructureType',
        label='appInfrastructureType',
        description='Contains the application infrastructure type.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:appInstanceType',
        label='appInstanceType',
        description='Contains the instance type.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:appServer',
        label='appServer',
        description='Contains application server.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:automationState',
        label='automationState',
        description='A value of \'Manual\' will mark a node as not eligible for Issue processing',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Automation:basicConfigId',
        label='basicConfigId',
        description='Contains the internal identifier of the basic configuration of a component .',
        valid='start=2015-05-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:brand',
        label='brand',
        description='Contains the brand of a component/device.',
        valid='start=2019-01-15;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:buildName',
        label='buildName',
        description='Contains the build name of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:buildType',
        label='buildType',
        description='Contains the build type of a component.',
        valid='start=2015-08-19;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:command',
        label='command',
        description='Contains an automation command.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:companyName',
        label='companyName',
        description='Contains the company name of a component.',
        valid='start=2015-11-02;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:contextPath',
        label='contextPath',
        description='Contains the context path of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuCoreCount',
        label='cpuCoreCount',
        description='Contains the number of cpu cores.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuCount',
        label='cpuCount',
        description='An integer which shows the number of cps of a component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuManufacturer',
        label='cpuManufacturer',
        description='Contains the manufacturer of the cpu of a device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuModel',
        label='cpuModel',
        description='Contains the model of the cpu.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuSpeed',
        label='cpuSpeed',
        description='An floating point number which shows the cpu speed in GHZ.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:cpuType',
        label='cpuType',
        description='Contains the cpu type of a device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:dataClassification',
        label='dataClassification',
        description='Data classification of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:dataPrivacy',
        label='dataPrivacy',
        description='Data privacy of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:databaseSchema',
        label='databaseSchema',
        description='Contains information about the database schema. The schema is the skeleton structure that represents the logical view of the entire database',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:databaseServer',
        label='databaseServer',
        description='Contains information about the database server.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:defaultRank',
        label='defaultRank',
        description='Contains the default rank for a KI ranking.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit.Automation:defaultSigma',
        label='defaultSigma',
        description='Contains the default sigma value for a KI ranking.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit.Automation:deployStatus',
        label='deployStatus',
        description='String value, represents the status if an automation Knowledge Item is not deployed into an Automation Engine.',
        valid='start=2016-01-25;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:deployToEngine',
        label='deployToEngine',
        description='Obsolete attribute. Not used for HIRO >=6. Boolean value, true if an automation Knowledge Item can deploy into an Automation Engine.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:diskCount',
        label='diskCount',
        description='An integer which shows the number of disks of a component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:diskSpace',
        label='diskSpace',
        description='An integer which contains the disk space in GB.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:domain',
        label='domain',
        description='Contains the domain name.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:environmentFilter',
        label='environmentFilter',
        description='Contains the specification/filtering of an environment.',
        valid='start=2019-04-01;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.Automation:exchangeRate',
        label='exchangeRate',
        description='Contains the data rate exchanged.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:firewallStatus',
        label='firewallStatus',
        description='Contains information about the firewall status.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:firmwareVersion',
        label='firmwareVersion',
        description='Version of the firmware.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:fqdn',
        label='fqdn',
        description='Contains a fully qualified domain name.',
        valid='start=2019-01-15;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:governingContract',
        label='governingContract',
        description='Contains information about the governing contract.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:host',
        label='host',
        description='Contains the host name.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:installCount',
        label='installCount',
        description='Contains an integer. This integer can be adjust automatically when software is added to or deleted from configuration items (CIs).',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:installPath',
        label='installPath',
        description='Contains the installation path of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:isDeployed',
        label='isDeployed',
        description='Obsolete attribute. Not used for HIRO >=6. Boolean value, true if an automation Knowledge Item is deployed into an Automation Engine.',
        valid='start=2016-01-25;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:issueFormalRepresentation',
        label='issueFormalRepresentation',
        description='Obsolete attribute. Not used for HIRO >=6. Contains an issue in XML representation defined by IssueSchema.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:issueType',
        label='issueType',
        description='Contains the type of the issue.',
        valid='start=2018-11-01;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit.Automation:knowledgeItemFormalRepresentation',
        label='knowledgeItemFormalRepresentation',
        description='Contains an automation Knowledge Item (KI) in XML representation defined by KiSchema.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:knowledgeItemId',
        label='knowledgeItemId',
        description='Obsolete attribute. Not used for HIRO >=6. Contains a KnowledgeItemID in string representation.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:knowledgeItemSyntaxVersion',
        label='knowledgeItemSyntaxVersion',
        description='Contains an automation Knowledge Item (KI) syntax version.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de')
    yield Attribute(
        about='ogit.Automation:knowledgeItemTier',
        label='knowledgeItemTier',
        description='Numeric value describing KnowledgeItem Tier.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:licenseAvailability',
        label='licenseAvailability',
        description='The availability of the license of a component.',
        valid='start=2015-07-24;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:licenseName',
        label='licenseName',
        description='Contains the license name of a component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:licenseType',
        label='licenseType',
        description='Contains the license type of a component.',
        valid='start=2015-05-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:lifecycle',
        label='lifecycle',
        description='Contains the lifecycle state of a MARSNode. If value is \'decommissioned\' this node is ignored by engine, graph and UI.',
        valid='start=2017-05-11;',
        created_by='Philipp Kählitz')
    yield Attribute(
        about='ogit.Automation:logLevel',
        label='logLevel',
        description='Contains the numeric log level of the history entry.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:maidFormalRepresentation',
        label='maidFormalRepresentation',
        description='Obsolete attribute. Not used for HIRO >=6. Contains a MAID in XML representation defined by MAIDSchema.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:mandatoryParameters',
        label='mandatoryParameters',
        description='Contains mandatory parameters as key/value mapping',
        valid='start=2019-04-01;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.Automation:marsNodeFormalRepresentation',
        label='marsNodeFormalRepresentation',
        description='Obsolete attribute. Not used for HIRO >=6. Contains MARS in XML representation defined by MARSSchema2013.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:marsNodeType',
        label='marsNodeType',
        description='Obsolete attribute. Not used for HIRO >=6. Contains The Type of the Mars Node. Should be one of Application, Machine, Software, Resource.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:maxIdleTime',
        label='maxIdleTime',
        description='Sets the maximum idle time of an AutomationIssue. HIRO Engine internally manages the idle time for each AutomationIssue. Whenever a KnowledgeItem gets applied it is reset to zero. If maximum idle time is reached the AutomationIssue is regarded as \'cannot be processed anymore until more knowledge is provided\'',
        valid='start=2019-07-22;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Automation:memory',
        label='memory',
        description='Contains a the total physical memory (RAM) in MB.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:middlewareType',
        label='middlewareType',
        description='Contains information about the type of middleware. For example it  database middleware, application server middleware or a message-oriented middleware.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:moveToProductionAt',
        label='moveToProductionAt',
        description='Defines the time when something was actually moved to production.\nThe values can combine date and time with time zone designator according to ISO 8601.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:objectIdentifier',
        label='objectIdentifier',
        description='Contains a system object identifier.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:optionalParameters',
        label='optionalParameters',
        description='Contains optional parameters as key/value mapping',
        valid='start=2019-04-01;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.Automation:originNode',
        label='originNode',
        description='Defines where an AutomationIssue starts/started its lifecycle. Must contain a valid vertex id. Replaces the free attribute \'/NodeID\'',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Automation:osKey',
        label='osKey',
        description='Product key for the Operating System.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.Automation:osLicense',
        label='osLicense',
        description='License of the Operating System.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.Automation:osManufacturer',
        label='osManufacturer',
        description='Contains the manufacturer of the operating system.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:osName',
        label='osName',
        description='Contains operating system name.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.Automation:osServicePack',
        label='osServicePack',
        description='Contains the service pack for the operating system.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.Automation:osVersion',
        label='osVersion',
        description='Version of the Operating System.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.Automation:parentIssue',
        label='parentIssue',
        description='Contains the ID of the issue which created this issue.',
        valid='start=2019-06-01;',
        created_by='cy@arago.co')
    yield Attribute(
        about='ogit.Automation:patchNumber',
        label='patchNumber',
        description='Contains a patch number.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:portNumber',
        label='portNumber',
        description='Contains a port number.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:portNumberListener',
        label='portNumberListener',
        description='Contains a port number listener.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:processingNode',
        label='processingNode',
        description='Defines where an AutomationIssue is currently being processed or was being processed last. Must contain a valid vertex id. Replaces the free attribute \'/CurrentNodeID\'',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Automation:processingTimestamp',
        label='processingTimestamp',
        description='Contains the timestamp indicating last time an aumation issue was processed.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:projectName',
        label='projectName',
        description='Contains the project name of a component.',
        valid='start=2015-11-02;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Automation:rankMap',
        label='rankMap',
        description='Contains KI ranking values.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit.Automation:rankingType',
        label='rankingType',
        description='Contains the type of KI ranking algorithm.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='Simple,DecisionService,Random,Precalculated')
    yield Attribute(
        about='ogit.Automation:sendData',
        label='sendData',
        description='Boolean flag whether issue data should be sent to decision service.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='true,false')
    yield Attribute(
        about='ogit.Automation:sendHistory',
        label='sendHistory',
        description='Boolean flag whether issue history should be sent to decision service.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='true,false')
    yield Attribute(
        about='ogit.Automation:serialNumber',
        label='serialNumber',
        description='Contains a the serial number of a device/component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:serviceClass',
        label='serviceClass',
        description='Contains the class of the service.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:serviceId',
        label='serviceId',
        description='Contains the Id of the service.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:serviceName',
        label='serviceName',
        description='Contains the name of a service.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:serviceStatus',
        label='serviceStatus',
        description='Contains the status of a service.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:serviceType',
        label='serviceType',
        description='Contains the Type of a service.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:servletClass',
        label='servletClass',
        description='Contains the class of the servlet.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:servletName',
        label='servletName',
        description='Contains the name if the servlet.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:software',
        label='software',
        description='A software component.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:softwareKey',
        label='softwareKey',
        description='Contains the key of a software.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:suspendUntil',
        label='suspendUntil',
        description='Contains the timestamp until which entity should not be processed by HIRO.',
        valid='start=2019-06-01;',
        created_by='cy@arago.co')
    yield Attribute(
        about='ogit.Automation:systemClass',
        label='systemClass',
        description='Contains the class of the system.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:systemType',
        label='systemType',
        description='Contains the type of the system.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:tcpPort',
        label='tcpPort',
        description='The tcp port.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:todo',
        label='todo',
        description='Boolean value, true if variable is todo variable.',
        valid='start=2015-02-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Automation:virtualMachineName',
        label='virtualMachineName',
        description='Contains the name of the virtual machine.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:virtualSystemName',
        label='virtualSystemName',
        description='Contains the name of the virtual system.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:virtualSystemType',
        label='virtualSystemType',
        description='Contains the type of the virtual system.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:webServer',
        label='webServer',
        description='Contains an webServer.',
        valid='start=2015-07-24;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Automation:webhook',
        label='webhook',
        description='a http callback (https://en.wikipedia.org/wiki/Webhook)',
        valid='start=2019-06-01;',
        created_by='arago GmbH')
    yield Attribute(
        about='ogit.Automation:weightMap',
        label='weightMap',
        description='Contains fingerprint weight values for a KI ranking.',
        valid='start=2018-05-01;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit:BatteryState',
        label='BatteryState',
        description='current battery state of the device.',
        valid='start=2019-03-22;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.CustomerSupport:allowAttachments',
        label='allowAttachments',
        description='Boolean flag indicating whether agents may add attachments to this entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:customFieldNames',
        label='customFieldNames',
        description='Set of Strings that correspond to free attribute names that are used as custom ticket field names.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:defaultGroupId',
        label='defaultGroupId',
        description='Integer indicating the default user group id.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:defaultOrganizationId',
        label='defaultOrganizationId',
        description='Integer indicating the default organization id.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:deleted',
        label='deleted',
        description='Boolean flag indicating an deleted entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:details',
        label='details',
        description='String may contains address or additional details regarding this entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:domainNames',
        label='domainNames',
        description='List of Strings that are owned by this entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:hasIncidents',
        label='hasIncidents',
        description='Boolean flag indicating whether this entity(ticket) has any associated incidents.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:htmlContent',
        label='htmlContent',
        description='String containing the content with HTML markup.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:lastLoginAt',
        label='lastLoginAt',
        description='Timestamp indicating last users login instant.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:locale',
        label='locale',
        description='Locale indicating preferred communication localization.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:metadata',
        label='metadata',
        description='Integer representing flags associated with this entity(comment).',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:multiFactorAuth',
        label='multiFactorAuth',
        description='Boolean flag indicating whether this entity(user) uses a factor of more then one authentication method.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:note',
        label='note',
        description='String may contains additional notes besides any details regarding this entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:privateCommentsOnly',
        label='privateCommentsOnly',
        description='Boolean flag indicating whether this entity(user) may only create internal private comments.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:public',
        label='public',
        description='Boolean flag indicating whether this entity(comment) is visible to requester.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:recipient',
        label='recipient',
        description='String containing an email address that this ticket was send to and received at.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:remoteId',
        label='remoteId',
        description='A constant unique identifier for remote instances that persists even if remoteURL changes. RFC 4122 https://tools.ietf.org/html/rfc4122',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:remoteType',
        label='remoteType',
        description='A type to distinguish remote service provider. E.g. Zendesk.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:remoteUrl',
        label='remoteUrl',
        description='A URL pointing to the source data. RFC 3986 https://tools.ietf.org/html/rfc3986',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:restrictedAgent',
        label='restrictedAgent',
        description='Boolean flag indicating whether this entity(user) has restricted agent access.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:role',
        label='role',
        description='String declaring whether this entity represents an end user, agent or admin.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:roleType',
        label='roleType',
        description='Integer representing a fine grained agent role.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:shareComments',
        label='shareComments',
        description='Boolean flag indicating whether this entity(organization) shares ticket comments with one or more third party Organization(s) via Service Provider infrastructure.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:shareTickets',
        label='shareTickets',
        description='Boolean flag indicating whether this entity(organization) shares tickets with one or more third party Organization(s) via Service Provider infrastructure.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:signature',
        label='signature',
        description='String contains a signature to be automatically appended onto ticket comments during submit.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:suspended',
        label='suspended',
        description='Boolean flag indicating whether this entity(user) has been banned from any further interaction.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:tags',
        label='tags',
        description='Set of Strings that have been declared for this entity.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:ticketRestriction',
        label='ticketRestriction',
        description='String indicating means of access control for tickets.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:timeZone',
        label='timeZone',
        description='String declaring this entity(user) time zone according to IANA notation',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.CustomerSupport:verified',
        label='verified',
        description='Boolean flag indicating whether this entity(user) has been verified by mail (opt in).',
        valid='start=2019-11-15;',
        created_by='Johannes Harth')
    yield Attribute(
        about='ogit.Data:timeToLive',
        label='timeToLive',
        description='Defines how many seconds data will be kept before expire.',
        valid='start=2018-02-09;',
        created_by='mglusiuk@arago.de')
    yield Attribute(
        about='ogit.DataProcessing:internalJobId',
        label='internalJobId',
        description='The job id of the running program',
        valid='start=2017-02-28;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.DataProcessing:outputType',
        label='outputType',
        description='The type of the output data stream',
        valid='start=2017-02-27;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.DataProcessing:parameters',
        label='parameters',
        description='The query parameters',
        valid='start=2017-02-27;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.DataProcessing:query',
        label='query',
        description='The query of the input data stream',
        valid='start=2017-02-27;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.DataProcessing:queryType',
        label='queryType',
        description='Type of the query of the input data stream',
        valid='start=2017-02-27;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.DataProcessing:state',
        label='state',
        description='The state of the program: idle, started, stopped',
        valid='start=2017-02-28;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit.Datacenter:datacenterId',
        label='datacenterId',
        description='ID of a Datacenter',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Datacenter:moveProductionDate',
        label='moveProductionDate',
        description='Date when an device is moved to production use.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Datacenter:rackId',
        label='rackId',
        description='ID of a rack within a datacenter.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Datacenter:rackUnit',
        label='rackUnit',
        description='The name of the RackUnit within a datacenter.',
        valid='start=2015-10-15;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.Datacenter:roomId',
        label='roomId',
        description='ID of a Room in a Datacenter.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Datacenter:sectionId',
        label='sectionId',
        description='ID of a datacenter section.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Documents:headers',
        label='headers',
        description='Contains the list of column headers of a spreadsheet.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Documents:rows',
        label='rows',
        description='Contains the rows of a spreadsheet.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:approachingCars',
        label='approachingCars',
        description='The number of approaching cars on the street.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:carLightStatus',
        label='carLightStatus',
        description='The traffic light status for cars.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:foodAccessible',
        label='foodAccessible',
        description='The accessibility status of food in the Crow example scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:foodKcal',
        label='foodKcal',
        description='The food calorie of food in the Crow example scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:foodType',
        label='foodType',
        description='The type offood in the Crow example scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Examples.Crow:pedestrianLightStatus',
        label='pedestrianLightStatus',
        description='The traffic light status for pedestrians.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Factory:equipmentNumber',
        label='equipmentNumber',
        description='A unique identifier of a piece of equipment.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:amount',
        label='amount',
        description='The amount of an item, set of items, or payment.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:companyCode',
        label='companyCode',
        description='The amount of an item, set of items, or payment.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:invoiceDate',
        label='invoiceDate',
        description='Date of an invoice.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:invoiceNumber',
        label='invoiceNumber',
        description='Identifier of an invoice.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:quantity',
        label='quantity',
        description='The amount of an item, set of items, or payment.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:transactionDate',
        label='transactionDate',
        description='Date of a transaction.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialAccounting:valueDate',
        label='valueDate',
        description='Effective value date of a transaction.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:ISIN',
        label='ISIN',
        description='International Securities Identification Number - a unique identifier for securities.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:acquisitionDate',
        label='acquisitionDate',
        description='The acquisition date of an investment position.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:amount',
        label='amount',
        description='The amount or number of a financial instrument or investment. Depending on the type of instrument, the amount can be specified e.g. as number or nominal value.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:currency',
        label='currency',
        description='Indicates the currency of a value, price, or cost.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:defaultDate',
        label='defaultDate',
        description='The date of default for a corporation.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:defaultStatus',
        label='defaultStatus',
        description='The default status of a corporation.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:enterpriseSize',
        label='enterpriseSize',
        description='The size of a corporation.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:issueDate',
        label='issueDate',
        description='The date on which a security has been issued.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:legalEntityIdentifier',
        label='legalEntityIdentifier',
        description='An identifier of a company (legal entity).',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:legalForm',
        label='legalForm',
        description='The legal form of a corporation.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:maturityDate',
        label='maturityDate',
        description='Maturity date of a financial instrument.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:nationalIdentifier',
        label='nationalIdentifier',
        description='A unique nationally defined identifier for a corporation.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:thirdPartyPriorityClaims',
        label='thirdPartyPriorityClaims',
        description='Any priority claims by third parties on the same financial protection (security).',
        valid='start=2019-11-06;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.FinancialMarket:value',
        label='value',
        description='The financial value of a financial instrument or investment. It is recommended to always specify a currency in addition to the value.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Forum:username',
        label='username',
        description='A unique username for a member of a Forum',
        valid='start=2015-04-27;',
        created_by='Chris Walker')
    yield Attribute(
        about='ogit.Health.Diagnostics:ICDCode',
        label='ICDCode',
        description='Code assigned to diagnoses of diseases and other health problems according to ICD (International Classification of Diseases and Related Health Problems). More information at https://icd.who.int/icd11refguide/en/index.html',
        valid='start=2021-01-21;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:appID',
        label='appID',
        description='UDI of App (if paired).',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:batteryLevel',
        label='batteryLevel',
        description='battery level of equipment.',
        valid='start=2020-09-15;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:batteryState',
        label='batteryState',
        description='current battery State.',
        valid='start=2020-09-15;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:birthyearRange',
        label='birthyearRange',
        description='Birth year in range ( “before 1910”, “1910-1920”).',
        valid='start=2020-09-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:equipmentID',
        label='equipmentID',
        description='UDI of an equipment, for example a Sensor Hub.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:equipmentState',
        label='equipmentState',
        description='current equipment State.',
        valid='start=2020-09-15;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:equipmentStateChangeTime',
        label='equipmentStateChangeTime',
        description='time when equipment state was updated (timestamp in millisecond).',
        valid='start=2020-09-15;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:errorCode',
        label='errorCode',
        description='Error code.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:firmwareVersion',
        label='firmwareVersion',
        description='Sensor Hub firmware version.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:liquidContactTime',
        label='liquidContactTime',
        description='liquid contact time.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:sensorID',
        label='sensorID',
        description='UDI of  bio sensor (= Test ID).',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:symptoms',
        label='symptoms',
        description='symptoms (enum).',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:testCompletedAt',
        label='testCompletedAt',
        description='timestamp of test completion.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:testCounter',
        label='testCounter',
        description='test counter (how often has this sensor been used - should always be 1!).',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:testDate',
        label='testDate',
        description='Date when Test is performed.',
        valid='start=2020-10-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:testMethod',
        label='testMethod',
        description='Test method (PCR, Antigen, Antibody).',
        valid='start=2020-10-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Health.Diagnostics:testResult',
        label='testResult',
        description='Test result (positive, negative, inconclusive).',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Health.Diagnostics:testStartedAt',
        label='testStartedAt',
        description='timestamp of test start.',
        valid='start=2020-08-14;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Knowledge:archived',
        label='archived',
        description='Boolean indicating whether the session is archived or not',
        valid='start=2019-07-26;',
        created_by='Vitaly Teremasov',
        validation_type=ValidatorType.FIXED,
        validation_parameter='true,false')
    yield Attribute(
        about='ogit.Location:city',
        label='city',
        description='The name of a city.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:country',
        label='country',
        description='The name of a country.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:residenceCountry',
        label='residenceCountry',
        description='The name of a residence country.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:state',
        label='state',
        description='The name of a state.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:streetName',
        label='streetName',
        description='The name of a street.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:streetNumber',
        label='streetNumber',
        description='The number of a street address.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Location:zipCode',
        label='zipCode',
        description='The zip code of a city.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.MARS.Application:class',
        label='class',
        description='Used to classifiy Application nodes. Replaces \'ResourceClass\' from MARS-Schema.\n\t\tReplaces \'ApplicationClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='Data,Development,Education,Enterprise,Financial,Media,Others')
    yield Attribute(
        about='ogit.MARS.Application:subClass',
        label='subClass',
        description='Allows to further classify applications. This can be used to match KnowledgeItems specific to a certain business domain. Replaces \'ApplicationSubClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='DataManagement,Datawarehouse,DigitalAssetManagement,DocumentManagementSystem,GeographicInformationSystem,ComputerAidedEngineering,Diagramming,HardwareEngineering,IntegratedDevelopmentEnvironment,ProductEngineering,Simulation,SoftwareEngineering,Testing,WebDevelopment,ClassroomManagement,Teaching,ApplicationSuite,AssetManagement,BusinessWorkflow,CustomerRelationshipManagement,Email,EnterpriseInfrastructure,EnterprisePortal,EnterpriseResourcePlanning,KnowledgeManagement,ProcessManagement,Accounting,Banking,ClearingSystems,Compliance,Controlling,FinancialModelling,RiskManagement,Trading,Animation,Blog,ComputerGraphics,ComputerAidedDesign,DesktopPublishing,DocumentAssembly,DocumentAutomation,InformationManagementPortal,MediaDevelopment,Presentation,SoundEditing,VideoEditing,FieldServiceManagement,ReferenceSystems,ReservationSystems,TransactionSystem')
    yield Attribute(
        about='ogit.MARS.Machine:class',
        label='class',
        description='Defines the \'class\' of a Machine MARS node. This is basically the Operation System name. Replaces \'MachineClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='AIX,Appliance,HPUX,Linux,Solaris,UNIX,Windows,BSD,Router,Switch,WiFi')
    yield Attribute(
        about='ogit.MARS.Machine:cpuArch',
        label='cpuArch',
        description='CPU architecture. On UNIX like systems it will be the output onf \'uname -m\'. Replaces \'MachineArchitecture\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='x86_32,x86_64,Sparc,PowerPC,Itanium,Appliance,MIPS,Alpha,SH-x,StrongARM')
    yield Attribute(
        about='ogit.MARS.Machine:distroName',
        label='distroName',
        description='The distro name of an Operation System. For Linux you will encounter things like: \'CentOS\', \'RedHat\', ... . Replaces \'OSName\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Machine:kernel',
        label='kernel',
        description='Describes the running Operating System kernel. For Linux systems this is usually the output of \'uname -s -v -r\'. Replaces \'OSKernel\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Machine:ram',
        label='ram',
        description='The available system memory in a machine. It starts with a number following by an optional unit character (\'M\' or \'G\'). If unit character is omitted then \'M\' shall be assumed. This is . Replaces \'HWRAM\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.REGEX,
        validation_parameter='^\\d+(|M|G)$')
    yield Attribute(
        about='ogit.MARS.Network:bindAddress',
        label='bindAddress',
        description='Usually an IP address. Defines the listening address for a software (server). Replaces \'NetworkIP\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:defaultGateway',
        label='defaultGateway',
        description='Defines the default gateway. In case of IPv4 dot-decimal notation shall be used. Replaces \'NetworkDefaultGW\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:fqdn',
        label='fqdn',
        description='A FQDN according to RFC 1035. Replaces \'FQDN\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:interfaceIP',
        label='interfaceIP',
        description='Specifies the configured IP address of all defined interfaces. It\'s a key\'ed list with the key to be defined in attribute ogit/MARS/Network/interfaceName of the same Machine node. In case of IPv4 addresses dot-decimal notation shall be used. Replaces \'NetworkInterfaceIP\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:interfaceMAC',
        label='interfaceMAC',
        description='Alloes to specifies the MAC address of all defined interfaces. It\'s a key\'ed list with the key to be defined in attribute ogit/MARS/Network/interfaceName of the same Machine node. Replaces \'NetworkInterfaceMAC\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:interfaceName',
        label='interfaceName',
        description='This defines the network interface within a system. It\'s always a list containing all the defined interfaces, e.g. \'lo0 eth0 eth1\'. Replaces \'NetworkInterface\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:interfacePrefixLength',
        label='interfacePrefixLength',
        description='Specifies the network prefix length (network mask) of all defined interfaces. It\'s a key\'ed list with the key to be defined in attribute ogit/MARS/Network/interfaceName of the same Machine node. The values are always number, e.g. a value of \'24\' in the context of IPv4 is equivalent to 255.255.255.0 in dot-decimal notation. Replaces \'NetworkInterfacePrefixLength\' and \'NetworkInterfaceNetmask\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:ipVersion',
        label='ipVersion',
        description='Alloes to specify the IP version for defined interfaces. It\'s a key\'ed list with the key to be defined in attribute ogit/MARS/Network/interfaceName of the same Machine node. It can be used to to indicate what to expectd in the corresponding entries of other network related attributes, e.g \'ogit/MARS/Network/interfaceIP\'. Replaces \'NetworkInterfaceType\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:port',
        label='port',
        description='A number indicating a network port (0..65535). Usually used define the listening port for a software (server). Replaces \'NetworkPort\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Network:protocol',
        label='protocol',
        description='Can be used to define the network protocol a service (software) is using. Typical values: \'tcp\', \'udp\'. Replaces \'NetworkProtocol\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Resource:class',
        label='class',
        description='Used to classifiy Resource nodes. Will contain values like: \'Backend\', \'Database\', and so on. Replaces \'ResourceClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de',
        validation_type=ValidatorType.FIXED,
        validation_parameter='Backend,Computation,ContentDelivery,CoreApplication,Database,Environment,Frontend,Infrastructure,Interface,Logistics,Middleware,Monitoring,PhysicalObject,Place,Process,Provider,Security,Service,Storage')
    yield Attribute(
        about='ogit.MARS.Software:class',
        label='class',
        description='Used to classifiy Software nodes. Will contain values like: \'DBMS\', \'WebServer\', \'DataProcessing\', and so on. Replaces \'SoftwareClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Software:installPath',
        label='installPath',
        description='Defines where a software is installed. Replaces \'SWInstallPath\' and \'BasePath\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Software:instanceId',
        label='instanceId',
        description='Allow to define some instance identifier for a Software node. Usually this is used to uniquely identify a cluster member. The value might be a composition of several attributes, e.g. <data-center-id>:<rack-id>. Replaces \'Instance\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Software:logPath',
        label='logPath',
        description='Defines where a software writes its logfiles. Replaces \'LogPath\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Software:serviceName',
        label='serviceName',
        description='Defines the service name for a software which can buse for administrative operations like start, stop, or status. E.g on RedHat Linux it would be the name of the service unit (without the .service extension). Replaces \'ServiceName\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.MARS.Software:subClass',
        label='subClass',
        description='Give each type of Software a unique name, e.g \'OpenLDAP\' or \'MSSharePointServer\'. This should be the primary matching variable for software specific automation (using KnowledgeItems). Replaces \'SoftwareSubClass\' from MARS-Schema',
        valid='start=2018-06-01;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.ML:activeVersion',
        label='activeVersion',
        description='currently active version of ML model.',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:attributesSchema',
        label='attributesSchema',
        description='Information about attributes of training data, for example, How many columns, which type (String/Interger)',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:endpoint',
        label='endpoint',
        description='endpoint of prediction model.',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:meta',
        label='meta',
        description='Meta infromation about machine learning model',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:requirements',
        label='requirements',
        description='required information such as name and Version of the machine learning Frameworks, z.B. keras+tensorflow 1.20',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:size',
        label='size',
        description='The size of training data. Number of rows or entries.',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:trainData',
        label='trainData',
        description='if training data < 10Mb, it can be stored directly in this attribute (for Example as JSON). Attachment can be used for larger amount of training data. However, one of the trainData or attachmentID should be used, not both',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:trainedFrom',
        label='trainedFrom',
        description='Node Id of Traindata',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.ML:trainingSummary',
        label='trainingSummary',
        description='summary about training the machine learning model',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.MRP:actionPeriod1',
        label='actionPeriod1',
        description='first period for storage actions',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:actionPeriod2',
        label='actionPeriod2',
        description='first period for storage actions',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:containerConditions',
        label='containerConditions',
        description='storage container conditions',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:genericNorm',
        label='genericNorm',
        description='a generic norm or standard',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:industryStandard',
        label='industryStandard',
        description='Industry Standard/Norm to apply to this entity',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:kindOfMaterialDetailed',
        label='kindOfMaterialDetailed',
        description='specific type of material',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:kindOfMaterialGeneric',
        label='kindOfMaterialGeneric',
        description='generic class of material',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:kzTCond',
        label='kzTCond',
        description='required temperature conditions',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:minimumRemainingShelfLife',
        label='minimumRemainingShelfLife',
        description='minimal remaining shelf life at delivery',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:partNumber',
        label='partNumber',
        description='A part number of a part or material',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:roomConditions',
        label='roomConditions',
        description='other room conditions',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:specificNorm',
        label='specificNorm',
        description='a specific norm / section of a generic norm',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:tempMax',
        label='tempMax',
        description='maximal recommended temperature for storage',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:tempMin',
        label='tempMin',
        description='minimal recommended temperature for storage',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:tempRef',
        label='tempRef',
        description='optimal temperature for storage',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:totalShelfLife',
        label='totalShelfLife',
        description='shelf life for storage',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.MRP:unitOfShelfLife',
        label='unitOfShelfLife',
        description='unit used for totalShelfLife',
        valid='start=2019-02-18;',
        created_by='Christian Schulz')
    yield Attribute(
        about='ogit.Mobile:RSSIcorrection',
        label='RSSIcorrection',
        description='rssi correction values for mobile phones.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:TXcorrection',
        label='TXcorrection',
        description='TX correction values for mobile phones.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:activationTime',
        label='activationTime',
        description='time when licence code is activated.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:appConfigMode',
        label='appConfigMode',
        description='app cofiguration mode, i.e debug, release.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:appPermissions',
        label='appPermissions',
        description='permission available for the application',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:appVersion',
        label='appVersion',
        description='mobile application version',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:bundleID',
        label='bundleID',
        description='bundle id of the application, i.e debug, release.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:category',
        label='category',
        description='TODO',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:criticality',
        label='criticality',
        description='TODO',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:cta',
        label='cta',
        description='call to action. describe action should be taken by app user',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:ctaTarget',
        label='ctaTarget',
        description='call to action target, for ex. web url',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:ctaType',
        label='ctaType',
        description='call to action type',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:deactivationTime',
        label='deactivationTime',
        description='time when licence code is deactivated.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:delivered',
        label='delivered',
        description='boolean value, set true if message is delivered to app.',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:deviceCode',
        label='deviceCode',
        description='This attribute contains a unique device code, which identifies a specific device.',
        valid='start=2020-09-28;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Mobile:deviceCodeName',
        label='deviceCodeName',
        description='device code names, for ex walleye for google pixel 2.',
        valid='start=2020-08-31;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:deviceModel',
        label='deviceModel',
        description='model of device',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:devicePlatform',
        label='devicePlatform',
        description='Platform of device i.e ios, android..',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:deviceType',
        label='deviceType',
        description='type of device such as Mobile, FOB...',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:distance',
        label='distance',
        description='distance between two device where application is installed',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:duration',
        label='duration',
        description='time duration of the connection',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:enctime',
        label='enctime',
        description='TODO',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:firebaseToken',
        label='firebaseToken',
        description='firebaseToken',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:headline',
        label='headline',
        description='headline for message',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:healthStatus',
        label='healthStatus',
        description='current health status about the person using the device',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:healthStatusUpdateTime',
        label='healthStatusUpdateTime',
        description='last time when health status was updated. UTC timestamp format',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:isActive',
        label='isActive',
        description='boolean flag. indicate if node is currenlty used',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:label',
        label='label',
        description='label for licence code.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:lastActive',
        label='lastActive',
        description='the last day when app was used.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:licenceCode',
        label='licenceCode',
        description='unique uuid number',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:locale',
        label='locale',
        description='locale code defined in which language message should be retuned',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:message',
        label='message',
        description='text for message',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:movementType',
        label='movementType',
        description='type of movement such as foot, bus, train',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:osRadio',
        label='osRadio',
        description='internal chipset or design identifier for mobile phones.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:osVersion',
        label='osVersion',
        description='operating system version on which application is installed',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:registrationType',
        label='registrationType',
        description='registration Type, to identify push notification service used, if yes then which one',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:riskScore',
        label='riskScore',
        description='risk score',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:subline',
        label='subline',
        description='Additional text providing more information',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:time',
        label='time',
        description='Time when connection started.',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.Mobile:uuid',
        label='uuid',
        description='uuid is unique identifier for application.',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.OSLC-automation:progress',
        label='progress',
        description='Represents the progress that has been made towards completion (e.g. of an AutomationRequest or AutomationResult). The value of this property can either be an integer (showing percentage completion) or a resource (for implementation-specific details, or future extension).',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:affectsPlanItem',
        label='affectsPlanItem',
        description='Change request affects a plan item. It is likely that the target resource will be an oslc_cm:ChangeRequest but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:affectsRequirement',
        label='affectsRequirement',
        description='Change request affecting a Requirement. It is likely that the target resource will be an oslc_rm:Requirement but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:approved',
        label='approved',
        description='Whether or not the Change Request has been approved.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:closeDate',
        label='closeDate',
        description='The date at which no further activity or work is intended to be conducted.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:closed',
        label='closed',
        description='Whether or not the Change Request is completely done, no further fixes or fix verification is needed.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:fixed',
        label='fixed',
        description='Whether or not the Change Request has been fixed.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:inprogress',
        label='inprogress',
        description='Whether or not the Change Request in a state indicating that active work is occurring.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:reviewed',
        label='reviewed',
        description='Whether or not the Change Request has been reviewed.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:status',
        label='status',
        description='Used to indicate the status of the change request based on values defined by the service provider. Most often a read-only property. Some possible values may include: \'Submitted\', \'Done\', \'InProgress\', etc.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:tracksChangeSet',
        label='tracksChangeSet',
        description='Tracks SCM change set resource. It is likely that the target resource will be an oslc_scm:ChangeSet but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:tracksRequirement',
        label='tracksRequirement',
        description='Tracks the associated Requirement or Requirement ChangeSet resources. It is likely that the target resource will be an oslc_rm:Requirement but that is not necessarily the case.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-change:verified',
        label='verified',
        description='Whether or not the resolution or fix of the Change Request has been verified.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:allowedValue',
        label='allowedValue',
        description='value allowed for a property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:defaultValue',
        label='defaultValue',
        description='A default value for property, inlined into property definition.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:hidden',
        label='hidden',
        description='A hint that indicates that property MAY be hidden when presented in a user interface.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:hintHeight',
        label='hintHeight',
        description='Values MUST be expressed in relative length units as defined in the W3C Cascading Style Sheets Specification (CSS 2.1) Em and ex units are interpreted relative to the default system font (at 100% size).',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:hintWidth',
        label='hintWidth',
        description='Values MUST be expressed in relative length units as defined in the W3C Cascading Style Sheets Specification (CSS 2.1) Em and ex units are interpreted relative to the default system font (at 100% size).',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:isMemberProperty',
        label='isMemberProperty',
        description='Used to define when a property is a member of a container, useful for query.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:label',
        label='label',
        description='Very short label for use in menu items.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:maxSize',
        label='maxSize',
        description='For String properties only, specifies maximum characters allowed. If not set, then there is no maximum or maximum is specified elsewhere.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:message',
        label='message',
        description='An informative message describing the error that occurred.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:name',
        label='name',
        description='Name of property being defined, i.e. second part of property\'s Prefixed Name.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:prefix',
        label='prefix',
        description='Namespace prefix to be used for this namespace.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:prefixBase',
        label='prefixBase',
        description='The base URI of the namespace.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:prefixDefinition',
        label='prefixDefinition',
        description='Defines a namespace prefix for use in JSON representations and in forming OSLC Query Syntax strings.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:readOnly',
        label='readOnly',
        description='true if the property is read-only. If omitted, or set to false, then the property is writable. Providers SHOULD declare a property read-only when changes to the value of that property will not be accepted after the resource has been created, e.g. on PUT/PATCH requests. Consumers should note that the converse does not apply: Providers MAY reject a change to the value of a writable property.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:rel',
        label='rel',
        description='If present and set to \'alternate\' then indicates that work-around is provided, behavior for other values is undefined.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:shortId',
        label='shortId',
        description='Shorter form of dcterms:identifier for the resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:shortTitle',
        label='shortTitle',
        description='Shorter form of dcterms:title for the resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:statusCode',
        label='statusCode',
        description='The HTTP status code reported with the error.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-core:totalCount',
        label='totalCount',
        description='This optional property indicates the total number of results across all pages,\n\t\tits value should be non-negative. In the context of a query resource, this value SHOULD\n\t\tbe the total number of results, i.e. the number of resources that match the query.\n\t\tIn the context of other resources, the value SHOULD be the total number of property\n\t\tvalues (i.e. RDF triples) of the resource. Unless Stable Paging is in effect, the\n\t\ttotal count MAY vary as a client retrieves subsequent pages.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:address',
        label='address',
        description='The canonical string representation of the IP address. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:fileName',
        label='fileName',
        description='The file name of the package containing the SoftwareModule.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:fqdn',
        label='fqdn',
        description='The fully qualified domain name (FQDN). In Internet communications, the name of a host system that includes all of the subnames of the domain name. An example of a fully qualified domain name is es123126.lab.ibm.com .',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:hostid',
        label='hostid',
        description='A globally unique ID assigned to their machines by some manufacturers (.e.g Sun Solaris) .',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:instancePath',
        label='instancePath',
        description='The directory where the files for this SoftwareServer are stored.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:ipAddress',
        label='ipAddress',
        description='The IP address assigned to this system.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:model',
        label='model',
        description='Value of the device model. The model number as provided by the device manufacturer.  ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:name',
        label='name',
        description='Typically used as an identity field, this property is used to represent a known name of a resource instance.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:observationTime',
        label='observationTime',
        description='The time that the resource was last observed by the provider.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:occursBefore',
        label='occursBefore',
        description='If there is a temporal order between other Path or ServiceInstance Resource Definitions, the Resource Definition action that occur after this Resource Instance are listed here. ',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:portNumber',
        label='portNumber',
        description='The port number as defined by IETF and IANA.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:processId',
        label='processId',
        description='The process id number assigned to the Process by the operating system.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:serialNumber',
        label='serialNumber',
        description='Serial number assigned by the manufacturer. The value should be provided by the manufacturer of the resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:shortHostName',
        label='shortHostName',
        description='A label assigned to a machine and used for communications on the local network. For example, a Windows hostname is IBM-2JMUUEH6TEQ .',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:systemBoardUUID',
        label='systemBoardUUID',
        description='The unique identifier of the system board.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:version',
        label='version',
        description='The version string assigned to this entity.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-crtv:vmid',
        label='vmid',
        description='The VMID is a unique identifier for the virtual machine.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:from',
        label='from',
        description='\nThis property links a mapping to its custom label value.\nThe value MUST be unique within its enclosing map resource.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:high',
        label='high',
        description='\nThis property gives the <em>high</em> parameter value of a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:isActive',
        label='isActive',
        description='\nThis boolean property indicates if a scenario is under active consideration.\nWhen a scenario has been ruled out, it is marked as inactive by setting this property to <code>false</code>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:isClosed',
        label='isClosed',
        description='This boolean property indicates if the project is closed.\nNo further activities or measurements are done on closed projects.\nThe measurements of closed projects can be used to calibrate the estimates for new projects.\nWhen a project is completed and all measurements on it have been performed,\nit is marked as closed by setting this property to <code>true</code>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:lambda',
        label='lambda',
        description='\nThis property gives the <em>lambda</em> parameter value of a Poission distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:low',
        label='low',
        description='\nThis property gives the <em>low</em> parameter value of a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:mostLikely',
        label='mostLikely',
        description='\nThis property gives the <em>most likely</em> parameter value of a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:numberOfQuantiles',
        label='numberOfQuantiles',
        description='\nThis property gives the <em>number of quantiles</em> parameter value of a probability distribution.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:numericValue',
        label='numericValue',
        description='This property gives the numeric value of a resource.\nFor example, the numeric value of the measure <em>duration of 12 months</em> is 12.\nThe datatype of this property is typically <code>xsd:double</code>.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:probability',
        label='probability',
        description='\nThis property gives the cumulative probability.\nFor example, the cumulative probability of the third quartile is 75%.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:realProjectId',
        label='realProjectId',
        description='This property links a project to an identifier of the project as a real-world object.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-ems:scale',
        label='scale',
        description='\nThis property gives the <em>scale</em> parameter value of a probability distribution.\nThis parameter is also known as the <em>standard deviation</em> and is often denoted by\nthe Greek letter sigma.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-perfmon:availabilityStatus',
        label='availabilityStatus',
        description='An indication of availability.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-perfmon:mobilityEnabled',
        label='mobilityEnabled',
        description='An indication about whether the resource can move about dynamically.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.OSLC-perfmon:tableReorganizationNeeded',
        label='tableReorganizationNeeded',
        description='Indicates whether a database\'s tables need to be reorganized.',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.PTF:callCnt',
        label='callCnt',
        description='How many calls were sended, e.g. for creating or reading nodes.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:clientCnt',
        label='clientCnt',
        description='Amount of concurrent clients.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:dbAwsMachineCnt',
        label='dbAwsMachineCnt',
        description='Amount of db-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:dbAwsMachineType',
        label='dbAwsMachineType',
        description='AWS Instance-Type of db-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:duration',
        label='duration',
        description='The duration of one performance test run without preperation time in seconds.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:endTime',
        label='endTime',
        description='The end time of one test in seconds.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:engineAwsMachineCnt',
        label='engineAwsMachineCnt',
        description='Amount of engine-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:engineAwsMachineType',
        label='engineAwsMachineType',
        description='AWS Instance-Type of engine-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:graphAwsMachineCnt',
        label='graphAwsMachineCnt',
        description='Amount of graph-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:graphAwsMachineType',
        label='graphAwsMachineType',
        description='AWS Instance-Type of graph-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:graphNodesCnt',
        label='graphNodesCnt',
        description='How many graph nodes were used.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:hiroVsn',
        label='hiroVsn',
        description='Version of HIRO installation.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:hotTest',
        label='hotTest',
        description='Whether if the test is a hot-test (true) or a cold-test (false).',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:iamAwsMachineCnt',
        label='iamAwsMachineCnt',
        description='Amount of iam-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:iamAwsMachineType',
        label='iamAwsMachineType',
        description='AWS Instance-Type of iam-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:issuesCnt',
        label='issuesCnt',
        description='How many issues were used.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:kisCnt',
        label='kisCnt',
        description='How many kis were used.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:linksCnt',
        label='linksCnt',
        description='How many links were used.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:revProxyAwsMachineCnt',
        label='revProxyAwsMachineCnt',
        description='Amount of rexProxy-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:revProxyAwsMachineType',
        label='revProxyAwsMachineType',
        description='AWS Instance-Type of revProxy-machines inside a cluster or all-in-one HIRO.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:startTime',
        label='startTime',
        description='The start time of one test in seconds.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:vertexSearchCount',
        label='vertexSearchCount',
        description='Amount of search items, expected response is just a number.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.PTF:vertexSearchFull',
        label='vertexSearchFull',
        description='Amount of search items, expected response is a whole document.',
        valid='start=2019-02-19;',
        created_by='Thomas Gotwig')
    yield Attribute(
        about='ogit.Price:discreteValue',
        label='discreteValue',
        description='Concrete value for the pricing element.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:factor',
        label='factor',
        description='Value of the factor.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:factorTarget',
        label='factorTarget',
        description='Where to apply the factor (Node/Tree/Attribute).',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:priceAmount',
        label='priceAmount',
        description='Amount to pay for example for an invoice.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:priceTimeUnit',
        label='priceTimeUnit',
        description='Unit price of the service per time unit (attribute timeUnitSeconds).',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:targetAttribute',
        label='targetAttribute',
        description='Attribute to which the factor will be applied to (If target == Attribute)',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Price:timeUnitSeconds',
        label='timeUnitSeconds',
        description='Time unit (in seconds) that price applies to. A time unit of 0 for a quantity means a one-time fee is charged. A time \nunit of 0 for an activity means the price is charged for every instance of the activity. All pricing elements of an \nattribute pricing must have the same time unit. The time unit is irrelevant for factor pricing elements.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Procurement:productionOrderId',
        label='salesOrderId',
        description='Identifier for a production order.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Procurement:purchaseOrderId',
        label='purchaseOrderId',
        description='Identifier for a purchase order.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.RDDL:purpose',
        label='purpose',
        description='Purpose is derived from xlink:arcrole',
        valid='start=2016-09-22;',
        hide=False,
        created_by='OGIT Importer')
    yield Attribute(
        about='ogit.RL:state',
        label='state',
        description='Specifies the state of the issue for Reinforcement Learning.',
        valid='start=2020-01-02;',
        created_by='Rudi Schäfer')
    yield Attribute(
        about='ogit.RL:totalReward',
        label='totalReward',
        description='Specifies the total reward of the issue for Reinforcement Learning.',
        valid='start=2020-01-02;',
        created_by='Rudi Schäfer')
    yield Attribute(
        about='ogit.RPA:Odometry',
        label='Odometry',
        description='Current absolute robot position, as measured from startup point.',
        valid='start=2019-03-22;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit.SalesDistribution:amount',
        label='amount',
        description='The amount of an item, set of items, or payment.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:customerId',
        label='customerId',
        description='Customer identifier.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:deliveryId',
        label='deliveryId',
        description='Identifier of a delivery.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:invoiceDate',
        label='invoiceDate',
        description='Date of an invoice.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:invoiceId',
        label='invoiceId',
        description='Identifier of an invoice.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:orderDate',
        label='orderDate',
        description='Date of a sales order.',
        valid='start=2019-08-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:salesOrderId',
        label='salesOrderId',
        description='Identifier for a sales order.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:shipmentId',
        label='shipmentId',
        description='Identifier for a shipment.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:transactionDate',
        label='transactionDate',
        description='Date of a transaction.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:transactionId',
        label='transactionId',
        description='Identifier of a payment transaction.',
        valid='start=2020-09-28;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.SalesDistribution:valueDate',
        label='valueDate',
        description='Effective value date of a transaction.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Schedule:attendanceStatus',
        label='attendanceStatus',
        description='Status of event attendence.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        validation_type=ValidatorType.FIXED,
        validation_parameter='accepted,declined,tentative,noResponse')
    yield Attribute(
        about='ogit.Schedule:dependencies',
        label='dependencies',
        description='Dependencies of a schedule activity.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Schedule:endTime',
        label='endTime',
        description='End time of a calendar event.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Schedule:isOrganizer',
        label='isOrganizer',
        description='Boolean indicating whether an attendee is the organizer of a calendar event.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        validation_type=ValidatorType.FIXED,
        validation_parameter='true,false')
    yield Attribute(
        about='ogit.Schedule:location',
        label='location',
        description='Location of a calendar event.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Schedule:resources',
        label='resources',
        description='Resources required for a schedule activity.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.Schedule:startTime',
        label='startTime',
        description='Start time of a calendar event.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit.ServiceManagement:allowedForNewBusiness',
        label='allowedForNewBusiness',
        description='If the value of this flag is true, the service could be offered in a store to new users for order. If flag is false, the service will only be available to users with already existing instances/entities of a specific service.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:approvalStatus',
        label='approvalStatus',
        description='Status of an ApprovalTask containing one of the following values: New|PendingApproval|Approved|Rejected|Cancelled|Closed.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='New,PendingApproval,Approved,Rejected,Cancelled,Closed')
    yield Attribute(
        about='ogit.ServiceManagement:changeStatus',
        label='changeStatus',
        description='Defines the status of a change record within the service management.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='New,Assigned,Pending,Resolved,ResolvedExternal,Closed,Escalated')
    yield Attribute(
        about='ogit.ServiceManagement:customer',
        label='customer',
        description='The customer related to a Service Management process.',
        valid='start=2015-07-03;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.ServiceManagement:elapsedTime',
        label='elapsedTime',
        description='Time between start time and now (minus pause duration).',
        valid='start=2015-06-08;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.ServiceManagement:eventMessage',
        label='eventMessage',
        description='Defines the event message/summary/logstring.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:eventNodeId',
        label='eventNodeId',
        description='Identifies the source of an event, i.e. identifies the monitoring endpoint which caused the event creation.\nThis could be an artifical identifier or some \"natural\" ID like hostname or IP address.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:externalTicketId',
        label='externalTicketId',
        description='If a ticket was imported/duplicated from another system this attribute will define the ticket ID from the source system.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:externalTicketSource',
        label='externalTicketSource',
        description='If a ticket was imported/duplicated from another system this will contain a string indentifying the source system.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:fallbackPlan',
        label='fallbackPlan',
        description='Defines instructions of how to revert in case a change fails.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:granularity',
        label='granularity',
        description='Smallest value increment of a Parameter',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:implementationPlan',
        label='implementationPlan',
        description='Used to define detail implementation instructions.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:incidentStatus',
        label='incidentStatus',
        description='Defines the status of an incident record/ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='New,Assigned,Pending,Resolved,ResolvedExternal,Closed,Escalated')
    yield Attribute(
        about='ogit.ServiceManagement:isRequired',
        label='isRequired',
        description='True if the value has to be specified for the Service to be provisioned. False otherwise.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:leftTime',
        label='leftTime',
        description='Time remaining until SLA breach.',
        valid='start=2015-06-08;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.ServiceManagement:licenseTokenStatus',
        label='licenseTokenStatus',
        description='The list of valid status values a license token can have',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='open,used,disabled')
    yield Attribute(
        about='ogit.ServiceManagement:problemStatus',
        label='problemStatus',
        description='defines the status of a problem record',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='New,Assigned,Pending,Resolved,ResolvedExternal,Closed')
    yield Attribute(
        about='ogit.ServiceManagement:reportedSource',
        label='reportedSource',
        description='Can be used to define how a ticket was communicated. It could define some kind of communication channel (\"ServiceDesk\", \"Email\") or, e.g. for Incident records, it might define that the ticket was produced automatically from an event management system.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:requirementId',
        label='requirementId',
        description='IDs of the corresponding requirements that lead to the entity creation.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:resolutionCode',
        label='resolutionCode',
        description='Optional resolution code that may be provied during an incident or problem along with the solution description.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:resolvedAt',
        label='resolvedAt',
        description='Datetime indicating when a ticket was resolved. Can be used for incident or problem tickets when it is necessary to distinguish between the ticket resolving and ticket closure (closedAt).\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:resolvedInTime',
        label='resolvedInTime',
        description='Information about a ticket being solved in the time excepted.',
        valid='start=2015-05-21;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit.ServiceManagement:rootCause',
        label='rootCause',
        description='Root cause for example of a problem ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:scheduledFinishAt',
        label='scheduledFinishAt',
        description='Defines a point in time when the work on a change is planned/scheduled to be finished. This date time is usually defined during change planning and/or approval.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:scheduledStartAt',
        label='scheduledStartAt',
        description='Defines a point in time when the work on a change is planned/scheduled to start. This date time is usually defined during change planning and/or approval. This datetime is set by change coordinater (e.g it  is planned to be done at 7:30PM)\nThe values must be combined date and time with time zone designator according to ISO 8601.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:slaStage',
        label='slaStage',
        description='Stage of an SLA.',
        valid='start=2015-06-08;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.ServiceManagement:solution',
        label='solution',
        description='Solution description, for example that is usually provided during incident resolving.\nThis field is also use for problem tickets. There is defines the permanent solution desription for a problem.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:sourceStatus',
        label='sourceStatus',
        description='It can be used to define application specific status values, which are not allowed by a normalized status, e.g. incidentStatus, changeStatus etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:targetFinishAt',
        label='targetFinishAt',
        description='Defines a point in time when the work on a change should be finished. This date time is defined by the requester.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:targetStartAt',
        label='targetStartAt',
        description='Defines a point in time when the work on a change should start. This date time is defined by the requester.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:task',
        label='task',
        description='A task related to a Service Management process.',
        valid='start=2015-07-06;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit.ServiceManagement:taskName',
        label='taskName',
        description='Contains the task name. It some cases it might be equal to taskID or to some short description (summary) of the task.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:taskStatus',
        label='taskStatus',
        description='Defines the status of a task.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='New,Assigned,Pending,Resolved,ResolvedExternal,Closed,Escalated')
    yield Attribute(
        about='ogit.ServiceManagement:testPlan',
        label='testPlan',
        description='Contains a test plan used in change management to define how a successful change implementation can be verified.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:ticketId',
        label='ticketId',
        description='ID of the ticket in the source system, e.g. the ID of the ticket in BMC.',
        valid='start=2015-05-26;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.ServiceManagement:workAround',
        label='workAround',
        description='Defines a work around for a known problem until a permanent solution is defined.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit.Version:major',
        label='major',
        description='major version according to https://semver.org/',
        valid='start=2018-05-25;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Version:minor',
        label='minor',
        description='minor version according to https://semver.org/',
        valid='start=2018-05-25;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit.Version:patch',
        label='patch',
        description='patch version according to https://semver.org/',
        valid='start=2018-05-25;',
        created_by='fotto@arago.de')
    yield Attribute(
        about='ogit:_c-id',
        label='_c-id',
        description='[internally generated] The content version id for Attachments',
        created_at='2019-08-06',
        modified_at='2019-08-06',
        valid='start=2015-05-27;',
        created_by='arago',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit:_content',
        label='_content',
        description='[internally generated] Used for the elastic search.',
        valid='start=2015-07-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_created-on',
        label='_created-on',
        description='[internally generated] Timestamp in ms when the node was created',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_creator',
        label='_creator',
        description='[internally generated] The id of the identity who created the node or edge',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_creator-app',
        label='_creator-app',
        description='[internally generated] App that creates nodes and edges.',
        valid='start=2015-07-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_deleted-by',
        label='_deleted-by',
        description='[internally generated] The id of the identity who did the deletion.',
        valid='start=2015-05-21;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit:_deleted-by-app',
        label='_deleted-by-app',
        description='[internally generated] App that deleted a graph element.',
        valid='start=2015-07-27;',
        created_by='cy@arago.de')
    yield Attribute(
        about='ogit:_deleted-on',
        label='_deleted-on',
        description='[internally generated] Timestamp in ms when the node was deleted',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_edge-id',
        label='_edge-id',
        description='[internally generated] contains the edge-id',
        valid='start=2015-07-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_graphtype',
        label='_graphtype',
        description='[internally generated] A virtual property which helps differentiating between graph objects. Values are \"edge\" or \"vertex\".',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_id',
        label='_id',
        description='[internally generated] The unique identifier. The id is automatically generated by GraphIT.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_is-deleted',
        label='_is-deleted',
        description='[internally generated] whether a node is deleted',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_modified-by',
        label='_modified-by',
        description='[internally generated] The id of the identity who did the modification',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_modified-by-app',
        label='_modified-by-app',
        description='[internally generated] App that modified nodes and edges.',
        valid='start=2015-07-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_modified-on',
        label='_modified-on',
        description='[internally generated] A timestamp in ms when the node was modified.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_organization',
        label='_organization',
        description='[internally generated] The id of the Auth/Organization that owns the data',
        valid='start=2018-01-01;',
        created_by='arago GmbH')
    yield Attribute(
        about='ogit:_owner',
        label='_owner',
        description='[internally generated] The id of the identity who owns the node',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_reader',
        label='_reader',
        description='[internally generated] The organization id with read access to this node',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_scope',
        label='_scope',
        description='[internally generated] The id of the Auth/DataScope that owns the data',
        valid='start=2018-01-01;',
        created_by='arago GmbH')
    yield Attribute(
        about='ogit:_source',
        label='_source',
        description='[internally generated] The installation id where the node originates from',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_tags',
        label='_tags',
        description='[internally generated] Used for individual search.',
        valid='start=2015-07-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_type',
        label='_type',
        description='[internally generated] The id of the type of the entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_v',
        label='_v',
        description='[internally generated] The vertex version number',
        created_at='2018-06-15',
        modified_at='2018-06-15',
        valid='start=2015-05-27;',
        created_by='cy@arago.de',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit:_v-id',
        label='_v-id',
        description='[internally generated] The vertex version id',
        created_at='2018-07-10',
        modified_at='2018-07-10',
        valid='start=2015-05-27;',
        created_by='cy@arago.de',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit:_version',
        label='_version',
        description='[internally generated] The ontology version number',
        valid='start=2015-05-27;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:_xid',
        label='_xid',
        description='a user provide id with limited uniqueness guarantees',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:accessControl',
        label='accessControl',
        description='The access control level of this Node. Value could mean different things to different\napplications / policies. Initial intent is that policies would treat \"public-read\"\n(inspired by Amazon AWS S3 ACLs) to mean anyone would have read-only access to this\nnode.',
        valid='start=2015-03-26;',
        created_by='Chris Walker')
    yield Attribute(
        about='ogit:acknowledgeState',
        label='acknowledgeState',
        description='Defines the state of acknowledgement.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:addressLocality',
        label='addressLocality',
        description='The locality belonging to an address. For example, Frankfurt am Main',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:admin-contact',
        label='admin-contact')
    yield Attribute(
        about='ogit:alternativeName',
        label='alternativeName',
        description='Alternative name of something. In context of a Person this can be the full name or an alias/nick name.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:asset',
        label='asset',
        description='This field represents an asset (device or component).',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:assetTag',
        label='assetTag',
        description='This field specifies the asset tag number/code.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:assignedAt',
        label='assignedAt',
        description='Defines the time when something was actually assigned to a person/organization for example.\nThe values can combine date and time with time zone designator according to ISO 8601.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:assignedGroup',
        label='assignedGroup',
        description='Assigned Group to a Service Management process.',
        valid='start=2015-07-01;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:attachmentID',
        label='attachmentID',
        description='Node Id for attachment node.',
        valid='start=2020-02-19;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit:availability',
        label='availability',
        description='Contains information about the availability of a service/device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:blob',
        label='blob',
        description='`blob` flag to allow different type to be attached with BLOB. Use it as ogit:blob true;')
    yield Attribute(
        about='ogit:brand',
        label='brand',
        description='Brand/Manufacturer of a component/device.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:buildingId',
        label='buildingId',
        description='ID of a Building.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:businessCategory',
        label='businessCategory',
        description='The category of a business.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:businessCriticality',
        label='businessCriticality',
        description='The business criticality of a process/service/CI.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:capacity',
        label='capacity',
        description='General Capacity',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:capacityAvailable',
        label='capacityAvailable',
        description='If the flag is true, then service can be ordered by new instance. If the flag is false, the service cannot temporarily be ordered due to capacity reasons.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:cardinality',
        label='cardinality')
    yield Attribute(
        about='ogit:category',
        label='category',
        description='Used to categorize things.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:certainty',
        label='certainty',
        description='Defines the certainty of an event',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:changeLog',
        label='changeLog',
        description='String value describing a changelog of an entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:checkedInAt',
        label='checkedInAt',
        description='Defines the time when something was actually checked in.\nThe values can combine date and time with time zone designator according to ISO 8601.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:checkedOutAt',
        label='checkedOutAt',
        description='Defines the time when something was actually checked out.\nThe values can combine date and time with time zone designator according to ISO 8601.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:ciType',
        label='ciType',
        description='Type of a configuration item. For example: VM, Server or Device.',
        valid='start=2015-08-20;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:city',
        label='city',
        description='Name of a city.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:class',
        label='class',
        description='Class of a component/device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:closedAt',
        label='closedAt',
        description='Will defined the time when a ticket was closed.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:color',
        label='color',
        description='Contains a color.',
        valid='start=2020-08-04;',
        created_by='Ben Neal')
    yield Attribute(
        about='ogit:comment',
        label='comment',
        description='Contains a comment.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:condition',
        label='condition',
        description='This field represents condition type.',
        valid='start=2018-03-22;',
        created_by='qikram@arago.de')
    yield Attribute(
        about='ogit:confidentiality',
        label='confidentiality',
        description='Contains information about the confidentiality related to a device or an entity.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:connectorId',
        label='connectorId',
        description='The Id of the connector.',
        valid='start=2015-06-11;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:consentLevel',
        label='consentLevel',
        description='formal agreement with contact.',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit:contact',
        label='contact',
        description='This field displays the device/CI/component owner who is the person assigned to the device/CI/component and uses it on a day-to-day basis. Support contacts are secondary contacts who may have access to a CI for example.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:content',
        label='content',
        description='A string holding any type of content: plain string, XML fragments, RDF documents, ...',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:country',
        label='country',
        description='Name of a country.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:createdAt',
        label='createdAt',
        description='Defines a point in time when a ticket/incident/event etc was created or recorded.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:creationTime',
        label='creationTime',
        description='Creation time of an entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:creator',
        label='creator',
        description='Creator of an entity.',
        valid='start=2015-08-20;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:currency',
        label='currency',
        description='A currency code, possibly according to ISO 4217.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:deadline',
        label='deadline',
        description='Defines a point in time when a deadline is reached.',
        valid='start=2016-12-19;',
        created_by='stravlos@arago.co')
    yield Attribute(
        about='ogit:deleter',
        label='deleter')
    yield Attribute(
        about='ogit:deliveredAt',
        label='deliveredAt',
        description='Defines a point in time when a component/device was actually delivered.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:description',
        label='description',
        description='Contains a description.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:duration',
        label='duration',
        description='This field represents a duration of an event, activity, phase, etc. It is recommended to use this attribute in conjunction with durationUnit.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit:durationUnit',
        label='durationUnit',
        description='This field specifies the unit of a duration, e.g. seconds, minutes, hours, days, or years.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit:effort',
        label='effort',
        description='Defines how much time was spent on the actual work for a change, task, or similar entity.\nThe values is expected to be in format HH:MM, e.g. 1:00 for 1 hour effort.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.REGEX,
        validation_parameter='^(\\d+:\\d\\d)$')
    yield Attribute(
        about='ogit:email',
        label='email',
        description='An email address.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:endOfWarranty',
        label='endOfWarranty',
        description='End of warranty phase of a component',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:enumValues',
        label='enumValues',
        description='The enumeration values for the parameter types represented by a JSON array.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:expirationDate',
        label='expirationDate',
        description='Defines a point in time when something becomes invalid the format is described at http://purl.org/goodrelations/v1#validThrough',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:expiresAt',
        label='expiresAt',
        description='Defines the date something expires.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:externalId',
        label='externalId',
        description='The External Id of a component.',
        valid='start=2015-05-21;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:faultCount',
        label='faultCount',
        description='Contains fault count related to a component',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:fax',
        label='fax',
        description='The number of a fax.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:finishedAt',
        label='finishedAt',
        description='Defines a point in time when the work on a change, task, or similar entity was actually finished.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:firstName',
        label='firstName',
        description='First name of a person',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:firstOccurredAt',
        label='firstOccurredAt',
        description='Defines the date of first occurrence of an event',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:frequency',
        label='frequency',
        description='This field specifies a frequency at which e.g. events occur.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit:function',
        label='function',
        description='Attibute used to specify a function that some entity does/provides.This is more specific then \'description\'.  \nShould contain a short string. At this level of specification it is still a free from string.\nHowever, unlike \'description\', it is expected to contain some list of fixed values.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:gender',
        label='gender',
        description='person\'s gender(sex). i.e male, female..',
        valid='start=2020-08-24;',
        created_by='Kaushik gondaliya')
    yield Attribute(
        about='ogit:hide',
        label='hide')
    yield Attribute(
        about='ogit:id',
        label='id',
        description='General id.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:impact',
        label='impact',
        description='Will contain the impact, for example of a ticket. In this case the actual semantics would depend on the ticket type, \nwhich could correspond to an Incident, Service Request, etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:information',
        label='information',
        description='Contains some informative string. Alternative to description attribute.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:installStatus',
        label='installStatus',
        description='An installation status for an entity.\nAt this level of specification no list of values is specified. However, applications using this attribute are expected to allow only a fixed list of values that seems usefual in the application\'s semantic context.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:installedAt',
        label='installedAt',
        description='Defines a point in time when a component/device was actually installed.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:instance',
        label='instance',
        description='Defines the name of an instance.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:integrity',
        label='integrity',
        description='A security pricipale that ensures data and Configuration Items are only modified by authorized personnel and Activities',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:inventoryNumber',
        label='inventoryNumber',
        description='This field specifies the inventory component number for the a device as defined by the company-defined  device inventory number in the model table.\nThe system uses this number to provide data on the Manufacturer, Model, and Version fields if available.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:invoiceNumber',
        label='invoiceNumber',
        description='Contains an invoice number. This number is used as identifier for security purposes.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:ipAddress',
        label='ipAddress',
        description='The IP address of a component/hardware device.',
        valid='start=2015-05-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:isCritical',
        label='isCritical',
        description='This field specifies if the CI is critical for day-to-day operation, such as an E-mail server or RDBMS server. \nIf you open an incident on a critical CI, the incident indicates that this is a critical CI. \nThis filed contains a boolean value.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:isInternal',
        label='isInternal',
        description='Boolean which can define internal data. The actual semantics depends on the usage context',
        valid='start=2019-02-01;',
        created_by='FCO',
        validation_type=ValidatorType.FIXED,
        validation_parameter='true,false')
    yield Attribute(
        about='ogit:isMutable',
        label='isMutable',
        description='True if the value can be changed. E.g. after a service is provisioned.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:isRoot',
        label='isRoot',
        description='Defines if an event is root.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:isSupported',
        label='isSupported',
        description='Indicates whether the service currently is supported.\nThis filed contains a boolean value.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:isValid',
        label='isValid',
        description='Boolean value, true if the object is valid.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:justification',
        label='justification',
        description='Justification for a ChangeRequest',
        valid='start=2015-07-01;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:language',
        label='language',
        description='A language code, possibly according to ISO 639.',
        valid='start=2018-12-05;',
        created_by='Viktor Voss')
    yield Attribute(
        about='ogit:lastClearedAt',
        label='lastClearedAt',
        description='Defines the date an event has been cleared.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:lastName',
        label='lastName',
        description='Last name of a person.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:lastOccurredAt',
        label='lastOccurredAt',
        description='Defines the date of last occurrence of an event',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:lastScannedAt',
        label='lastScannedAt',
        description='Defines a point in time when a component/device was actually scanned last time.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:lastUpdatedAt',
        label='lastUpdatedAt',
        description='Defines latest date and time when a ticket or it\'s comment was updated. The format of this value could be according to ISO 8601.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:lastUpdatedBy',
        label='lastUpdatedBy',
        description='Defines the last person or process who updated an entity.',
        valid='start=2015-07-20;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:latitude',
        label='latitude',
        description='It is a geographic coordinate that specifies the north–south position of a point on the Earth\'s surface..',
        valid='start=2020-08-24;',
        created_by='Kaushik gondaliya')
    yield Attribute(
        about='ogit:leaseContract',
        label='leaseContract',
        description='This field specifies the lease contract covering a service.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:lengthOfReportingPeriod',
        label='lengthOfReportingPeriod',
        description='Period in which the attribute is reported.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:licenseId',
        label='licenseId',
        description='The id of the license to be used to fetch licenses.',
        valid='start=2017-09-06;',
        created_by='Oday Jubran')
    yield Attribute(
        about='ogit:licenseKey',
        label='licenseKey',
        description='A string containing a license key.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:licenseRequestStatus',
        label='licenseRequestStatus',
        description='The list of valid status values a license request can have.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        validation_type=ValidatorType.FIXED,
        validation_parameter='pending,send,error,approved,rejected,failed,received,cancelled,closed')
    yield Attribute(
        about='ogit:licenseType',
        label='licenseType',
        description='Type of the License e.g. community/enterprise.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:locationAcquisitionTime',
        label='locationAcquisitionTime',
        description='Timestamp (with millisecond resolution) of acqusition of location..',
        valid='start=2020-08-24;',
        created_by='Kaushik gondaliya')
    yield Attribute(
        about='ogit:locationPrecision',
        label='locationPrecision',
        description='Estimated precision (in meters) of location.',
        valid='start=2020-08-24;',
        created_by='Kaushik gondaliya')
    yield Attribute(
        about='ogit:locked',
        label='locked',
        description='A lock state for an  entity.\nAt this level of specification no list of values is specified. However, applications using this attribute are expected to allow only a fixed list of values that seems usefual in the application\'s semantic context.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH')
    yield Attribute(
        about='ogit:longitude',
        label='longitude',
        description='It is a geographic coordinate that specifies the east–west position of a point on the Earth\'s surface.',
        valid='start=2020-08-24;',
        created_by='Kaushik gondaliya')
    yield Attribute(
        about='ogit:macAddress',
        label='macAddress',
        description='The mac address of a component.',
        valid='start=2015-05-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:maintenanceState',
        label='maintenanceState',
        description='Defines the state of maintenance.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:manufacturer',
        label='manufacturer',
        description='Manufacturer of a device or component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:market',
        label='market',
        description='Indicates market, for which an entity may be applicable.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:message',
        label='message',
        description='Contains a message.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:middleName',
        label='middleName',
        description='Middle name of a person.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:mobilePhone',
        label='mobilePhone',
        description='A mobile phone number.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:mode',
        label='mode',
        description='Contains the type of filter for the value contained in the entity \"Attribute\" and corresponding to one of the following strings: \neq, ne, lt, le, gt, ge, exists, notexists, string, notstring, regex, notregex',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:model',
        label='model',
        description='Model of a device.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:modelNumber',
        label='modelNumber',
        description='ModelNumber of a device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:modificationTime',
        label='modificationTime',
        description='Modification time.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:name',
        label='name',
        description='Contains a name.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:notification',
        label='notification',
        description='A notification.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:occurenceCount',
        label='occurenceCount',
        description='Defines the number an event occured.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:officePhone',
        label='officePhone',
        description='The phone number in the office.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:onAttribute',
        label='onAttribute',
        description='This field represents an attribute on which an event occured.',
        valid='start=2018-03-22;',
        created_by='qikram@arago.de')
    yield Attribute(
        about='ogit:onVertex',
        label='onVertex',
        description='This field represents a vertex on which an event occured.',
        valid='start=2018-03-22;',
        created_by='qikram@arago.de')
    yield Attribute(
        about='ogit:ontologyAdminContact',
        label='ontologyAdminContact',
        description='The \"admin-contact\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyAnyAttributes',
        label='ontologyAnyAttributes',
        description='The \"any-attributes\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyCardinality',
        label='ontologyCardinality',
        description='The \"cardinality\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyCreated',
        label='ontologyCreated',
        description='The \"created\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyCreator',
        label='ontologyCreator',
        description='the \"creator\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyDeleter',
        label='ontologyDeleter',
        description='The \"deleter\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyDescription',
        label='ontologyDescription',
        description='the \"description\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyHide',
        label='ontologyHide',
        description='Indicates if this part of ontology should hidden from the documentation',
        valid='start=2015-06-01;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyId',
        label='ontologyId',
        description='The \"id\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyModified',
        label='ontologyModified',
        description='the \"modified\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyName',
        label='ontologyName',
        description='the \"name\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyParent',
        label='ontologyParent',
        description='The \"parent\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyScope',
        label='ontologyScope',
        description='Indicates the ontology scope which could be either \"SGO\" or \"NTO\".',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyTechContact',
        label='ontologyTechContact',
        description='the \"tech-contact\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyType',
        label='ontologyType',
        description='Indicates the ontology type, which could be one of: \"entity\", \"attribute\", \"verb\"',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyValidFrom',
        label='ontologyValidFrom',
        description='The \"valid-from\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyValidUntil',
        label='ontologyValidUntil',
        description='The \"valid-until\" attribute as defined in OGIT yaml files.',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyValidationParameter',
        label='ontologyValidationParameter',
        description='The \"validation parameter\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:ontologyValidationType',
        label='ontologyValidationType',
        description='the \"validation-type\" attribute as defined in OGIT yaml files',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:openedAt',
        label='openedAt',
        description='Time when a ticket or task was created/opened.\nThe values could combine date and time with time zone designator according to ISO 8601 for service management tickets.\nFor most tickets there is no real difference between creation and opened time. In case such a distinction is relevant the \"createdAt\" attribute can be used.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:operation',
        label='operation',
        description='This field represents operation type.',
        valid='start=2018-03-22;',
        created_by='qikram@arago.de')
    yield Attribute(
        about='ogit:operationalStatus',
        label='operationalStatus',
        description='An operational status for an entity.\nAt this level of specification no list of values is specified. However, applications using this attribute are expected to allow only a fixed list of values that seems usefual in the application\'s semantic context.',
        valid='start=2015-05-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:orderedAt',
        label='orderedAt',
        description='Defines a point in time when a component/device was actually ordered.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:otherPhone',
        label='otherPhone',
        description='The number of an other phone.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:parent',
        label='parent')
    yield Attribute(
        about='ogit:pendingChange',
        label='pendingChange',
        description='This field indicates whether or not there are any changes pending against a component/device. When you close or open a change for this component/device, this action sets or clears the flag..',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:phone',
        label='phone',
        description='a phone number',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:placement',
        label='placement',
        description='A place where the object is placed.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Attribute(
        about='ogit:plannedFinishDate',
        label='plannedFinishDate',
        description='Defines the date when something will be finished.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Attribute(
        about='ogit:plannedStartDate',
        label='plannedStartDate',
        description='Defines the date when something will be started.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Attribute(
        about='ogit:position',
        label='position',
        description='Indicates user\'s position. This field contains a string value.',
        valid='start=2016-10-18;',
        created_by='Arthur Shoba')
    yield Attribute(
        about='ogit:positionNumber',
        label='positionNumber',
        description='An integer, which displays a position of numbering.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:postalCode',
        label='postalCode',
        description='The postal code. For example, 60433.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:powerConsumption',
        label='powerConsumption',
        description='Power consumption of a device.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:priority',
        label='priority',
        description='Priority of a ticket. The actual semantics might depend on the ticket type (Incident, Service Request, ...)',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:productOrderNumber',
        label='productOrderNumber',
        description='An integer, which displays the order number of a product.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:project',
        label='project',
        description='Project name, for which the entity is being used.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:purchaseDate',
        label='purchaseDate',
        description='Date of purchase of a device.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:purchasedAt',
        label='purchasedAt',
        description='Defines a point in time when a component/device was actually purchased.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:question',
        label='question',
        description='Contains a question.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:range',
        label='range',
        description='A range of numbers (a number in the range).',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:rank',
        label='rank',
        description='The rank of an item within an ordered list.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer')
    yield Attribute(
        about='ogit:reason',
        label='reason',
        description='Describes the reason for a decision.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:reportedAt',
        label='reportedAt',
        description='Defineds the time when something was actually reported.\nThe values can combin date and time with time zone designator according to ISO 8601.\nReported time is used in incident management in the following manner: in most cases the reported time equals the time when the incident is created. In some cases, e.g. the incident is created after the helpdesk has already worked on some request before it was decided to create an incident, the reported time might differ from ticket creation/opening time.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:resource',
        label='resource',
        description='Defines the name of an resource on an instance e.g. disk or database.',
        valid='start=2016-08-03;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:response',
        label='response',
        description='Contains the response for a question.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:reviewedAt',
        label='reviewedAt',
        description='Defines the time when something was actually reviewed.\nThe values can combin date and time with time zone designator according to ISO 8601.\nReviewed time is used in incident management.',
        valid='start=2015-07-01;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:revision',
        label='revision',
        description='Contains the revision of versioned data.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de')
    yield Attribute(
        about='ogit:risk',
        label='risk',
        description='Used to store the result of a risk analysis.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:schedule',
        label='schedule',
        description='Schedule represented by a string in cron format.',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev')
    yield Attribute(
        about='ogit:scope',
        label='scope')
    yield Attribute(
        about='ogit:securityClass',
        label='securityClass',
        description='Contains the security class of an entity/device.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:serialNumber',
        label='serialNumber',
        description='A string representing a any kind of serial number. see http://purl.org/goodrelations/v1#serialNumber',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:serviceContract',
        label='serviceContract',
        description='This field specifies the contract covering a service.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:severity',
        label='severity',
        description='Stores a severity. E.g. Some event management systems might store a severity field.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:shortDescription',
        label='shortDescription',
        description='Contains a short description.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:size',
        label='size',
        description='The size, e.g. of a file.',
        valid='start=2015-03-26;',
        created_by='arago Technologies')
    yield Attribute(
        about='ogit:source',
        label='source',
        description='source of data, string value.',
        valid='start=2020-08-27;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit:sourceId',
        label='sourceId',
        description='The Id of the source system.',
        valid='start=2015-06-11;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:sourceTable',
        label='sourceTable',
        description='Contains the source table, that stores where the data are coming from.',
        valid='start=2015-08-20;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:soxClass',
        label='soxClass',
        description='This attribute specifies, if an entity has a Sarbanes Oxley (SOX) classification that applies to it. The out-of-box data is: Critical or Non Critical',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:startedAt',
        label='startedAt',
        description='Defines a point in time when the work on a change, task, or similar entity was actually started.\nThe values must be combined date and time with time zone designator according to ISO 8601',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:status',
        label='status',
        description='A status for an entity.\nAt this level of specification no list of values is specified. However, applications using this attribute are expected to allow only a fixed list of values that seems usefual in the application\'s semantic context.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:streetAddress',
        label='streetAddress',
        description='The street address. For example, Eschersheimer Landstr. 526-532',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:subCategory',
        label='subCategory',
        description='Used to give a subcategory to  things.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:subType',
        label='subType',
        description='A subtype of an an entity.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:subject',
        label='subject',
        description='Contains the subject.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:summary',
        label='summary',
        description='A summary/short description, for example of a ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:taskLog',
        label='taskLog',
        description='In cases where the log for a Task is maintained as a single string it will be stored in taskLog.\nIn all other case consider using ogit/Timeseries.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:tech-contact',
        label='tech-contact')
    yield Attribute(
        about='ogit:timestamp',
        label='timestamp',
        description='Contains the timestamp in milliseconds.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:title',
        label='title',
        description='Title of any kind. In the context of a Person this can be a courtesy title, an academic title, or a job tilte.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:token',
        label='token',
        description='A unique randomly created ID to make communication between client and vendor possible during the process of requesting a license',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:type',
        label='type',
        description='Type of an an entity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:unit',
        label='unit',
        description='Unit of measurement of some value.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:updateCount',
        label='updateCount',
        description='Contains the count of the records updated.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:urgency',
        label='urgency',
        description='Contains the urgency which could be appliead to a ticket, incident etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:uri',
        label='uri',
        description='Unified resource identifier',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:url',
        label='url',
        description='Contains an URL (unified resource locator)',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:validFrom',
        label='validFrom',
        description='Defines a point in time when something becomes valid.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:validTo',
        label='validTo',
        description='Defines a point in time when something stops being valid.',
        valid='start=2016-11-29;',
        created_by='stravlos@arago.co')
    yield Attribute(
        about='ogit:validation-parameter',
        label='validation-parameter')
    yield Attribute(
        about='ogit:validation-type',
        label='validation-type')
    yield Attribute(
        about='ogit:value',
        label='value',
        description='Contains a value of a key / value pair.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:values',
        label='values',
        description='Represents a list of values. How to actually encode a list of values is left to the semantics of the entities using this attribute.',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:vendor',
        label='vendor',
        description='Contains the vendor of a device or software/hardware component.',
        valid='start=2015-07-27;',
        created_by='Aymen Ayoub')
    yield Attribute(
        about='ogit:version',
        label='version',
        description='Any string representation of version information. no restrictions are imposed on that base attribute',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:webPage',
        label='webPage',
        description='A web page.',
        valid='start=2015-07-27;',
        created_by='Philipp Pelchmann')
    yield Attribute(
        about='ogit:weight',
        label='weight',
        description='Physical weight of an entity, e.g. device/component/rack',
        valid='start=2015-05-21;',
        created_by='Peter Larem')
    yield Attribute(
        about='ogit:yearOfBirth',
        label='yearOfBirth',
        description='Birth year of person.',
        valid='start=2020-08-24;',
        created_by='Kaushik Gondaliya')
    yield Attribute(
        about='ogit:zipCode',
        label='zipCode',
        description='zip code or postal code of area.',
        valid='start=2020-03-16;',
        created_by='Kaushik Gondaliya')
    # </editor-fold>


# noinspection SpellCheckingInspection
def entity_data() -> Generator[Entity, None, None]:
    # <editor-fold desc="generated entity data">
    yield Entity(
        about='ogit:Account',
        label='Account',
        description='A account can be e.g. an facebook-account.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Accounting:CategoryItem',
        label='CategoryItem',
        description='Category Item is a Financial Statement Item',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:CompanyEntity',
        label='CompanyEntity',
        description='For example: Group, Legal Entity...',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:CompanySpecificCategorization',
        label='CompanySpecificCategorization',
        description='Categorization Map for Categorizing Line Items',
        valid='start=2018-12-05;',
        created_by='Gibson Xavier',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:ConfigItem',
        label='ConfigItem',
        description='ConfigItem is a company specific template or mapping',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:DDTarget',
        label='DDTarget',
        description='Due Diligences target company',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:FinancialStatement',
        label='FinancialStatement',
        description='For example: Trial Balance...',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Accounting:LineItem',
        label='LineItem',
        description='Line Item is a Financial Statement Item',
        valid='start=2018-12-05;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:Advertiser',
        label='Advertiser',
        description='The advertiser.',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:Campaign',
        label='Campaign',
        description='An advertising campaign',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:CampaignManager',
        label='CampaignManager',
        description='Manages end-to-end campaign',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:Client',
        label='Client',
        description='Client purchasing advertising from agency',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:Creative',
        label='Creative',
        description='The ad content',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:InsertionOrder',
        label='InsertionOrder',
        description='The individual order or purchase to be sent out to a publisher',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:LineItem',
        label='LineItem',
        description='Individual advertising orders on insertion order - lowest level',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:MediaPlan',
        label='MediaPlan',
        description='The advertising plan, what to buy, when, what conditions etc.',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Advertising:Platform',
        label='Platform',
        description='Platform or application on which a Campaign is run',
        valid='start=2019-05-10;',
        created_by='Patrick Williamson',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Alert',
        label='Alert',
        description='Alerts are used to notify users if certain events happen.',
        valid='start=2016-10-26;',
        created_by='stravlos@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Asset',
        label='Asset',
        description='Assets represent a physical hold of a value and are situated in a location. Assets could correspond to one or more \nogit/Automation/MARSNode\'s and can be physical or virtual. Assets of a Service Provider include anything that could \ncontribute to the delivery of a Service. Assets can have a type, for example: Management, Organisation, Process, \nKnowledge, People, Information, Applications, Infrastructure, Financial Capital.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Attachment',
        label='Attachment',
        description='This entity defines a file attachment that an IT service, issue, task or a ticket might have. The attachment itself is \nnot saved in GraphIT, instead it contains an external url link for it.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Audit:Audit',
        label='Audit',
        description='A specific audit project.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Audit:Batch',
        label='Batch',
        description='A batch of samples to audit.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Audit:Sample',
        label='Sample',
        description='A sample to audit.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Account',
        label='Account',
        description='An account is used for authentication and authorization.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:AccountProfile',
        label='AccountProfile',
        description='A profile associated with an account.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Application',
        label='Application',
        description='An Application is used for authorization.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:ApplicationReview',
        label='ApplicationReview',
        description='Represents an application review',
        created_at='2018-05-18',
        modified_at='2018-05-18',
        valid='start=2018-05-18;',
        created_by='Mikhail Osher',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Configuration',
        label='Configuration',
        description='An ogit/Auth/Configuration reflects individual configuration for an organization registered in hiro knowledge core',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:DataScope',
        label='DataScope',
        description='An ogit/Auth/DataScope is used to separate data between different engine instances',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:DataSet',
        label='DataSet',
        description='An ogit/Auth/DataSet defines set of data for authorization purposes',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:OrgDomain',
        label='OrgDomain',
        description='Allows Customer to have multiple valid email domains',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Organization',
        label='Organization',
        description='An ogit/Auth/Organization reflects a real world organization registered in hiro knowledge core',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Role',
        label='Role',
        description='An Role is used for authorization.',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:RoleAssignment',
        label='RoleAssignment',
        description='An ogit/Auth/RoleAssignment links team, role, and dataset to grant permissions',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Auth:Team',
        label='Team',
        description='A team is used to reflect the organizational structure of an ogit/Auth/Organization',
        created_at='2018-01-01',
        modified_at='2018-01-01',
        valid='start=2018-01-01;',
        created_by='arago GmbH',
        admin_contact='arago GmbH',
        tech_contact='arago GmbH',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:ActionApplicability',
        label='ActionApplicability',
        description='Defines the applicability of an action handler, such\n\tas `on ogit/_id`.',
        valid='start=2019-04-01;',
        created_by='Oday Jubran',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:ActionCapability',
        label='ActionCapability',
        description='Defines the capability of an action handler, such\n\tas remote execution via ssh.',
        valid='start=2019-04-01;',
        created_by='Oday Jubran',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:ActionHandler',
        label='ActionHandler',
        description='ActionHandler entity, that is connected to Configuration, one or more Capability, and Applicability nodes.',
        valid='start=2019-04-01;',
        created_by='Oday Jubran',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:AutomationIssue',
        label='AutomationIssue',
        description='Dynamic information exists within an automation engine in the form of Issues otherwise referred to as\nTask or Situational Data. From the technical perspective an Issue is a number of attributes (Key/Value tuples) with\nunique names. From the logical point of view Issues contain information about the change of states on a system.\nIssues can be injected into an automation engine from external systems e.g. Monitoring or result from the execution of a Knowledge Item.\nBy comparing an Issue with the Issue Condition of a Knowledge Item an automation engine decides which Knowledge Items are are processed\nin which order. If multiple Knowledge Items can be applied to an Issue the KI with the more precisely defined\nIssueCondition is processed first.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:Configuration',
        label='Configuration',
        description='Configuration node to dynamically connect Knowledge Pools or Rankings to a HIRO installation.',
        valid='start=2018-04-25;',
        created_by='cy@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:DynamicEngineData',
        label='DynamicEngineData',
        description='Dynamic information exists within the arago Automation Engine (aAE) used to store volatile data about current state of MARSNode or AutomationIssue.',
        valid='start=2015-06-25;',
        created_by='Miroslaw Glusiuk',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:History',
        label='History',
        description='IssueHistoryEntry corresponds to element <HistoryEntry> from IssueOutputSchema.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:Item',
        label='Item',
        description='Item describing a condition for an automation issue (e.g. Request) that would correspond to a technical characteristic, \nwhich would activate the automation Trigger.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:KIRanking',
        label='KIRanking',
        description='A specific knowledge ranking configuration for HIRO.',
        valid='start=2018-04-25;',
        created_by='cy@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:KnowledgeBundle',
        label='KnowledgeBundle',
        description='A grouping of `ogit/Automation/KnowledgeItem`s into a package.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:KnowledgeItem',
        label='KnowledgeItem',
        description='Formalized Knowledge stored in XML format. Serves as the building block for automation solutions.\n\nA KnowledgeItem is a knowledge module, which is applied for execution of an issue.\nA KnowledgeItem checks therefor the information and decides if it will be executed.\nIn that case, the KnowledgeItem executes operations, which serves the exploitation of information.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:KnowledgeItemAttribute',
        label='KnowledgeItemAttribute',
        description='Contains key-value pairs (together with mode) found inside Issue subitems.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:KnowledgePool',
        label='KnowledgePool',
        description='A grouping of `ogit/Automation/KnowledgeItem`s and `ogit/Automation/KnowledgeBundle`s for user or automation engine.',
        valid='start=2015-04-27;',
        created_by='druss@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:MAID',
        label='MAID',
        description='The Monitoring-Automation Interface Description (MAID) is an abstract definition of\n\n\n1. a timeseries to be monitored\n\n2. desired normalizations of that timeseries\n\n3. a set of condition->event mappings to apply to the timeseries or its normalizations\n\n\n These time series definitions can be parameterized for more flexibility. Usually each MAID should describe \nexactly one raw timeseries. Depending of the type of monitoring or event management system connected to \nthe engine, the corresponding adapter may choose to either supply the raw timeseries itself or directly \ncreate issues using the contained Event structures if it the raw data is not available.\n\n\nThe abstract MAID definitions are then mapped to the MARS model within the engine using so-called \"Binding Blocks\".\n\n\nThus MAID ensures that the arago Automation Engine is compatible to any monitoring system and can fully interact \nwith them. By formalizing the interface the information verification process and definition of required add-ons \nto the monitoring systems becomes possible.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:MARSModel',
        label='MARSModel',
        description='A collection of MARSNodes allows to address all MARS nodes belonging together in a certain way at once the relationship \nfrom MARSModel to MARSNode is \'ogit/contains\'.\nexamples are: All MARS nodes describing the IT of one data center, or all MARS nodes associated with the same contract. \nIn such cases you would connect the other entity (data center, contract) with the MARSModel node instead creating links \nto any MARSNode being part of that model.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:MARSModelTemplate',
        label='MARSModelTemplate',
        description='Represents a set of interconnected MARSNodes, which will be used to define a vendor implementation template of an ordered \nservice offering.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:MARSNode',
        label='MARSNode',
        description='Using this entity type to represent MARS nodes is deprecated. New applications should prefer the entity types from ogit/MARS NTO.\n\nIT Objects will be representated in MARS Modell with MARS nodes.\nThe MARS model builds upon four basic types of objects with a single type of relationship. Basically the objects\nwhich are in fact called \"nodes\" represent both views - the business perspective and the technical view.\nThe technical components are modeled in the machine and software layers while the application and resource layers\ndescribe the business view of the IT environment.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:MARSNodeTemplate',
        label='MARSNodeTemplate',
        description='Entity similar to MARSNode but used to create ogit/Automation/MARSTemplate\'s, which are used to define a vendor implementation template of an ordered \nservice offering and to enable definition of cost elements (ogit/Cost/CostElement) attached to it. Automation/MarsNode can not be reused for template reasons.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:Trigger',
        label='Trigger',
        description='Trigger of a KI having a set of Subitems.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Automation:Variable',
        label='Variable',
        description='Variable definition to be used in KnowledegeItem',
        valid='start=2015-02-09;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Catalog',
        label='Catalog',
        description='Any kind of catalog which could be offered by an Organization (e.g. corresponding to a vendor). Might contain products, services, books, etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:CatalogItem',
        label='CatalogItem',
        description='An entry within a Catalog. the semantics of Item is more general than that of http://purl.org/goodrelations/v1#ProductOrService',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Certificate',
        label='Certificate',
        description='This enables storing information about existing certificates as vertices.',
        valid='start=2017-09-05;',
        created_by='Oday Jubran',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Comment',
        label='Comment',
        description='Defines comments for a ticket, issue or another type of entity. Also known as WorkLog, ChangeLog or HistoryEntry.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Configuration',
        label='Configuration',
        description='An entity reflects individual configuration for an instance',
        valid='start=2020-11-15;',
        created_by='Kaushik Gondaliya',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:ConfigurationItem',
        label='ConfigurationItem',
        description='A configuration item.',
        valid='start=2015-06-11;',
        created_by='Aymen Ayoub',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Contract',
        label='Contract',
        description='General definition of a contract. Usually used for IT service related contracts but at this level of detail it is not restricted to those.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Cost:Budget',
        label='Budget',
        description='The budget covers the CostElement. It is a list of all the money an Organisation or Business Unit plans to receive, and plans to pay out, over a specified period of time. For a general overview: see the NTO description on github.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Cost:CostDistribution',
        label='CostDistribution',
        description='Auxiliary structure to express the influence of CostElements on one another. For more detailed explanation please check definition of the entity ogit/CostModel/CostElement and for a general overview: see the NTO description on github.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Cost:CostElement',
        label='CostElement',
        description='The cost element is a type of cost for an activity, an ordered service or a business unit or budget. There are 3 levels of cost elements: Top Level, Middle Level, Bottom Level. Between the different levels, for each cost element there could be two types of edges: Incoming and Outgoing. Each type of edge could have two types of connections: consistsOf and contributesTo. E.g. a cost element CPU consists in 30% of a HR cost element. The HR cost element contributes in 40% to the cost of the CPU cost element. This percentage values will then be saved in the entity Distribution, which will be connected to the cost element. For a general overview: see the NTO description on github.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Cost:PlanningParameter',
        label='PlanningParameter',
        description='A Planning Parameter describes a Planning Template. It will contain a concrete value of a Parameter and the statistics derived from the expected distribution as attributes. For a general overview: see the NTO description on github.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Cost:PlanningTemplate',
        label='PlanningTemplate',
        description='A Planning Template is an estimated planning of cost elements referring to an Implementation Template and a Planning Parameter. It will consist of a recursive set of sub-templates, connected through an edge, where each one of them will represent a service. For a general overview: see the NTO description on github.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Course',
        label='Course',
        description='Any kind of course',
        valid='start=2017-04-19;',
        created_by='stravlos@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Credit:Contract',
        label='Contract',
        description='A contract, representing a deal, for a loan',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:Counterparty',
        label='Counterparty',
        description='A counterparty in a credit transaction.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:CounterpartyMutable',
        label='CounterpartyMutable',
        description='Mutable data for a counterparty of a loan',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:EconomicActivity',
        label='EconomicActivity',
        description='A category of economic activities in the context of Credit.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:Instrument',
        label='Instrument',
        description='An instrument issued by corporation in the context of credit.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:InstrumentMutable',
        label='InstrumentMutable',
        description='Mutable data for an instrument',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:InstrumentType',
        label='InstrumentType',
        description='A type of instruments in the context of credit.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:JointLiability',
        label='JointLiability',
        description='A JointLiability amount, a shared liability for a contract and a loan',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:Protection',
        label='Protection',
        description='A protection for a loan',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:ProtectionMutable',
        label='ProtectionMutable',
        description='Mutable data for a protection for a loan',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:ProtectionType',
        label='ProtectionType',
        description='A type of protection in the context of credit.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Credit:Purpose',
        label='Purpose',
        description='A purpose for a contract in the context of credit.',
        valid='start=2019-11-27;',
        created_by='Ola Irgens Kylling',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:CustomApplicationData',
        label='CustomApplicationData',
        description='Entity to store custom application data, a storage place not connected to any other entity and therefore isolated from \nthe global ontology. The storage of data through this entity is discouraged due to low performance.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.CustomerSupport:Comment',
        label='Comment',
        description='Represents a comment that relates to another entity. They may have attached files with optional thumbnails. E.g. a Ticket.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.CustomerSupport:Group',
        label='Group',
        description='Represents a collection of entities. E.g. Users.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.CustomerSupport:Organization',
        label='Organization',
        description='Represents an Organization that employs User Groups.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.CustomerSupport:Ticket',
        label='Ticket',
        description='Represents a Customer Support Ticket',
        valid='start=2019-11-15;',
        created_by='Johannes Harth',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.CustomerSupport:User',
        label='User',
        description='Represents a person with associated identities, preferences, roles and meta data.',
        valid='start=2019-11-15;',
        created_by='Johannes Harth',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Data:Log',
        label='Log',
        description='This entity defines a log. It used to store a sequence of log records',
        valid='start=2017-06-14;',
        created_by='stravlos@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.DataProcessing:DataView',
        label='DataView',
        description='Data view.',
        valid='start=2017-10-31;',
        created_by='druss@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.DataProcessing:Program',
        label='Program',
        description='The program is used for creating data streams,\n\t\tand applying transformations to them.',
        valid='start=2017-02-28;',
        created_by='Oday Jubran',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Building',
        label='Building',
        description='A physical Building within a location',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Cooling',
        label='Cooling',
        description='A physical Cooling Unit used for data centers and computer rooms',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Datacenter',
        label='Datacenter',
        description='Represents a datacenter',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:PowerDistributionUnit',
        label='PowerDistributionUnit',
        description='A PDU is a physical device for connecting datacenter devices with power sources',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Rack',
        label='Rack',
        description='A physical rack housing datacenter equipment',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Room',
        label='Room',
        description='A physical Room within a Building',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Section',
        label='Section',
        description='A physical/logical Section within a Room',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Sensor',
        label='Sensor',
        description='A sensor is a device that measures a physical quantity and converts it into a \'signal\' which can be read by an observer or by an instrument.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Server',
        label='Server',
        description='A physical/logical Server',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:Storage',
        label='Storage',
        description='A physical/logical Storage Unit',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Datacenter:UPS',
        label='UPS',
        description='A physical UPS device (Uninterruptible power supply)',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Device',
        label='Device',
        description='Any type of device',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Documents:Document',
        label='Document',
        description='A generic document. The specific document type should be specified in the ogit:type attribute.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Documents:Spreadsheet',
        label='Spreadsheet',
        description='A spreadsheet document.',
        valid='start=2020-02-07;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Email',
        label='Email',
        description='Any type of email adress.',
        valid='start=2016-01-22;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Entity',
        label='Entity',
        description='Represents the class of all Entities',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Environment',
        label='Environment',
        description='An environment describes the overall structure a user, computer or program operates in.',
        valid='start=2018-02-08;',
        created_by='Viktor Voss',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Event',
        label='Event',
        description='This entity defines any type of event records, e.g. ITSM/produced by event management systems, Business Process etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Examples.Crow:Crossing',
        label='Crossing',
        description='A pedestrian crossing with a traffic light.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Examples.Crow:Food',
        label='Food',
        description='A food item in the Crow example demo scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Examples.Crow:Scene',
        label='Scene',
        description='The scene representation of the Crow example demo.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Examples.Crow:Sidewalk',
        label='Sidewalk',
        description='A sidewalk in the Crow example demo scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Examples.Crow:Street',
        label='Street',
        description='A street in the Crow example demo scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Examples.Crow:Tree',
        label='Tree',
        description='A tree in the example demo scenario.',
        valid='start=2019-09-20;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Action',
        label='Action',
        description='An action performed at a machine or component of a manufacturing plant.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Component',
        label='Component',
        description='A machinery or equipment component of a factory.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Factory',
        label='Factory',
        description='A factory in a producing company.',
        valid='start=2018-10-19;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Failure',
        label='Failure',
        description='A failure of a manufacturing plant, machinery component or equipment.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Machine',
        label='Machine',
        description='TODO.',
        valid='start=2018-10-19;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:Plant',
        label='Plant',
        description='A manufacturing plant, which may consist of multiple machinery and equipment components.',
        valid='start=2019-12-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:ProductionLine',
        label='ProductionLine',
        description='TODO.',
        valid='start=2018-10-19;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:StorageInventory',
        label='StorageInventory',
        description='TODO.',
        valid='start=2018-10-19;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Factory:StorageTank',
        label='StorageTank',
        description='TODO.',
        valid='start=2018-10-19;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Invoice',
        label='Invoice',
        description='An invoice in the accounts payable process.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:InvoiceLineItem',
        label='InvoiceLineItem',
        description='An individual item on an invoice.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Payment',
        label='Payment',
        description='A payment in the accounts payable process.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Vendor',
        label='Vendor',
        description='A vendor in the accounts payable process.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting:Company',
        label='Company',
        description='Represents a company in the context of financial accounting.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialAccounting:OrganizationalUnit',
        label='OrganizationalUnit',
        description='An organizational unit within a company.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:AggregatedContracts',
        label='AggregatedContracts',
        description='A aggregated representation of multiple financial contracts in the context of financial markets. This is usually ',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Contract',
        label='Contract',
        description='A contract for a financial instrument sold by corporation in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Corporation',
        label='Corporation',
        description='A corporation in the context of financial markets.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Country',
        label='Country',
        description='A country in the context of financial markets.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:EconomicActivity',
        label='EconomicActivity',
        description='A category of economic activities in the context of financial markets.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Exchange',
        label='Exchange',
        description='An exchange in the financial markets, e.g. a stock exchange.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:FinancialInstrument',
        label='FinancialInstrument',
        description='A financial instrument issued by corporation in the context of financial markets.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:FinancialInstrumentCategory',
        label='FinancialInstrumentCategory',
        description='A category of financial instruments in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Index',
        label='Index',
        description='A financial index the context of financial markets.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:InstitutionalSector',
        label='InstitutionalSector',
        description='A category of institutional sector in the context of financial markets.',
        valid='start=2019-11-11;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Investment',
        label='Investment',
        description='An investment into a financial instrument.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Investor',
        label='Investor',
        description='An investor in the context of financial markets.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:LineOfBusiness',
        label='LineOfBusiness',
        description='A line of business within a corporation in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Portfolio',
        label='Portfolio',
        description='A portfolio of financial instruments in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Project',
        label='Project',
        description='A project which acts on the financial markets (e.g. to receive loans).',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:Protection',
        label='Protection',
        description='A protection (e.g. security) for financial contracts in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.FinancialMarket:ProtectionType',
        label='ProtectionType',
        description='A type of protection for financial contracts in the context of financial markets.',
        valid='start=2019-11-06;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Award',
        label='Award',
        description='Something which is won. A \'badge of merit\' or an achievement, etc...',
        valid='start=2015-04-23;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Banner',
        label='Banner',
        description='Standout content, i.e. a header, hero-unit or part of a carousel.\nExamples:\n    http://getbootstrap.com/examples/carousel/ (a carousel of banners)\n    http://getbootstrap.com/examples/jumbotron/ (the content at the top is a banner)',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Configuration',
        label='Configuration',
        description='Configuration Data. No Schema - all free attributes',
        valid='start=2015-04-23;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:FeedEntry',
        label='FeedEntry',
        description='A single entry in a newsfeed or other stream of items. Unlikely to contain many attributes of\nits own, more likely to link users with items describing the event.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Group',
        label='Group',
        description='A Node to associate a profile to a particular group',
        valid='start=2015-12-03;',
        created_by='bmoore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Invite',
        label='Invite',
        description='Invite is used to request participation with a node',
        valid='start=2015-09-02;',
        created_by='bmoore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:KnowledgeBundle',
        label='KnowledgeBundle',
        description='Deprecated in favor of `ogit/Automation/KnowledgeBundle`. A grouping of `ogit/Automation/KnowledgeItem`s into a package. ',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:KnowledgeBundleHistory',
        label='KnowledgeBundleHistory',
        description='A point-in-time snapshot of an `ogit/Forum/KnowledgeBundle`',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:KnowledgeItemHistory',
        label='KnowledgeItemHistory',
        description='Deprecated in favor of `ogit/VersioningData`. A data container of `ogit/Automation/KnowledgeItem`s changes.',
        valid='start=2015-11-13;',
        created_by='bmmore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Permission',
        label='Permission',
        description='Permission is used to approve a Nodes interaction with another Node',
        valid='start=2015-09-04;',
        created_by='bmoore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Post',
        label='Post',
        description='A Post is an online publication. Could be a blog post, or a posting on a forum/messageboard.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Profile',
        label='Profile',
        description='A User\'s persona within a forum. Linked to an `ogit/Identity` but separate, the Profile is\nthe root node for most operations with a Forum.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Rating',
        label='Rating',
        description='Rating is used to rank nodes based on an arbitrary integer `value`',
        valid='start=2015-08-12;',
        created_by='bneal@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Reply',
        label='Reply',
        description='A response to a some other entity',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Review',
        label='Review',
        description='A review to a some other entity',
        valid='start=2018-01-08;',
        created_by='bmoore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Role',
        label='Role',
        description='A Node to associate a profile with a particular Role within a Group',
        valid='start=2015-12-03;',
        created_by='bmoore@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:ShortId',
        label='ShortId',
        description='A Reference to another Entity, used to track access via a specific channel/referrer.\nFor example in TabTab, a Post has many shortIds which relate to different sharing\nmethods, e.g. one for Twitter, one for Yammer, one for Email, etc... TabTab uses them\nas \'short urls\' in the App and redirect the user to the correct content after tracking\nthe access by the channel (`ogit/function`) attribute. The `ogit/function` attribute\nis used for this as the function of this shortId is to track a specific channel of\ninbound traffic. The ShortId can be used without this channel/referrer data, albeit\nto more limited use.\nThe `ogit/id` attribute in this instance would be a short URL safe string.',
        valid='start=2015-04-23;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Tag',
        label='Tag',
        description='A Tag used to categorise content. The required `key` attribute should be used\nas the unique identifier, and the `name` considered a display name.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Topic',
        label='Topic',
        description='A Topic is a SubForum with a specific topic associated. Use to divide forums into\nsub-forums. However the entity is general enough to be used for anything that has\na given subject.',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:Workflow',
        label='Workflow',
        description='A Workflow defines a series of steps that must be completed in order.',
        valid='start=2017-09-18;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:WorkflowStep',
        label='WorkflowStep',
        description='A Workflow Step defines part of a workflow',
        valid='start=2017-09-18;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Forum:WorkflowTemplate',
        label='WorkflowTemplate',
        description='A WorkflowTemplate defines a series of steps that must be completed in order.',
        valid='start=2017-09-18;',
        created_by='bneal@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Applicant',
        label='Applicant',
        description='One who applies for a role',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Education',
        label='Education',
        description='qualification awarded to students upon successful completion of a course or study',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Recruiter',
        label='Recruiter',
        description='One who recruits',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Relevance',
        label='Relevance',
        description='define importance for the skill, for ex, High, Meidum, Low, Required',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya ',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Resume',
        label='Resume',
        description='A summary of education, employment experiences and qualifications',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:RoleTitle',
        label='RoleTitle',
        description='contains similar titles for job roles',
        valid='start=2019-04-02;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Score',
        label='Score',
        description='Score for each job role and resume',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:Skill',
        label='Skill',
        description='A skill is an ability to perform an activity in a competent manner.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:SkillGroup',
        label='SkillGroup',
        description='A group of skills',
        valid='start=2019-03-21;',
        created_by='Florian Fluegel',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.HR.Recruiting:WorkHistory',
        label='WorkHistory',
        description='contains previous work history for the resume',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:Anamnesis',
        label='Anamnesis',
        description='Anamnesis (Demographics)',
        valid='start=2020-08-14;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:Demographics',
        label='Demographics',
        description='Demographics data of user',
        valid='start=2020-09-15;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:Equipment',
        label='Equipment',
        description='Test Equipment (Sensor Hub). UDI of Sensor Hub is saved in the _xid attribute',
        valid='start=2020-08-14;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:Laboratory',
        label='Laboratory',
        description='Test Laboratory',
        valid='start=2020-08-14;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:Test',
        label='Test',
        description='Test',
        valid='start=2020-08-14;',
        created_by='Viktor Voss',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Health.Diagnostics:TestStation',
        label='Test Station',
        description='A station where diagnostics tests can be performed.',
        valid='start=2020-09-28;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Hyperlink',
        label='Hyperlink',
        description='A representation of an (optionally) titled Hyperlink to some media. No protocol restrictions imposed.',
        valid='start=2015-06-09;',
        created_by='cwalker@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Installation',
        label='Installation',
        description='This entity type allows to store information about installations.',
        valid='start=2018-08-14;',
        created_by='Oday Jubran',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Knowledge:AcquisitionRoom',
        label='AcquisitionRoom',
        description='Entity to describe a part of Knowledge Acquisition Session, linking to Conversation',
        valid='start=2019-01-03;',
        created_by='arabtsau@klika-tech.com',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Knowledge:AcquisitionSession',
        label='AcquisitionSession',
        description='Entity to describe a Knowledge Acquisition Session, linking to Conversation, Structured Task Steps and the Knowledge',
        valid='start=2017-03-14;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Knowledge:Step',
        label='Step',
        description='this is the description of a single - hopefully atomic - step in (potentially multi-step) process',
        valid='start=2017-03-14;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:License',
        label='License',
        description='This entity type allows to store license information or actual licenses.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:LicenseRequest',
        label='LicenseRequest',
        description='This allows clients to place a request for a license.\nUsually some license admin personnel will use the information from such a request to create the actual license.\nA request might contain a valid LicenseToken to indicate that this request is pre-approved.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:LicenseToken',
        label='LicenseToken',
        description='This serves as a placeholder for pre-approved license request it will be subsituted by a real license throughout the licence request process.\nThis will created by a license admin and communicated to potential licence requesters.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Location',
        label='Location',
        description='A place where some some service is offered or requested. In many cases this will be related to a an address of an \nOrganization. Similar to http://purl.org/goodrelations/v1#Location',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Location:Address',
        label='Address',
        description='A street address.',
        valid='start=2019-08-23;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Location:NUTSLevel1',
        label='NUTSLevel1',
        description='A region at the level 1 of the NUTS (Nomenclature of Territorial Units for Statistics) classification, representing a subdivision of a country.',
        valid='start=2020-09-04;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Location:NUTSLevel2',
        label='NUTSLevel2',
        description='A region at the level 2 of the NUTS (Nomenclature of Territorial Units for Statistics) classification, representing a subdivision of a country.',
        valid='start=2020-09-04;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Location:NUTSLevel3',
        label='NUTSLevel3',
        description='A region at the level 3 of the NUTS (Nomenclature of Territorial Units for Statistics) classification, representing a subdivision of a country.',
        valid='start=2020-09-04;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MARS:Application',
        label='Application',
        description='Vertices of this type are the \'A\'-nodes in the MARS model. \'A\' stands for \'Application\' and those nodes form the highest layer in the A-R-S-M layer model. An \'Application\' node groups \'Resource\' nodes which form one business application.',
        valid='start=2018-06-01;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MARS:Machine',
        label='Machine',
        description='Vertices of this type are the \'M\'-nodes in the MARS model. \'M\' stands for \'Machine\' and those nodes form the bottom layer in the A-R-S-M layer model. But to be precise a \'Machine\' node models any operation system instance (regardless whether running on bare metal or in some virtualized environment)',
        valid='start=2018-06-01;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MARS:Resource',
        label='Resource',
        description='Vertices of this type are the \'R\'-nodes in the MARS model. \'R\' stands for \'Resource\' and those nodes form the second highest layer in the A-R-S-M layer model. A \'Resource\' node groups \'Software\' nodes. It\'s up the user whether this grouping is used to to group software instance of the same software (e.g. all instances of an Oracle RAC) or software instance of different softwares (functional grouping, e.g. \'persistence\')',
        valid='start=2018-06-01;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MARS:Software',
        label='Software',
        description='Vertices of this type are the \'S\'-nodes in the MARS model. \'S\' stands for \'Software\' and those nodes form the second lowest layer in the A-R-S-M layer model. It\'s up to the user whether it will model a specific instance of a software (linked to just one \'Machine\' node) or several identical instances (then the \'Software\' node will be linked to several \'Machine\' nodes',
        valid='start=2018-06-01;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ML:PredictionModel',
        label='PredictionModel',
        description='trained Prediction model which can be used by client directly.',
        valid='start=2020-02-18;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ML:TrainedModel',
        label='TrainedModel',
        description='Trained machine learning model.',
        valid='start=2020-02-18;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ML:TrainingData',
        label='TrainingData',
        description='Training data for machine learning model.',
        valid='start=2020-02-18;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Aircraft',
        label='Aircraft',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:AircraftType',
        label='AircraftType',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Airport',
        label='Airport',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Bay',
        label='Bay',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Capability',
        label='Capability',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Component',
        label='Component',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Facility',
        label='Facility',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Layover',
        label='Layover',
        description='The IL-Check (intermediate layover check) is – in addition to the D-Check – one of the biggest, most elaborate aircraft overhauls.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:MPD',
        label='MPD',
        description='Maintenance Planning Data  documents data developed by the manufacturer of a particular airplane that contains the information each operator of that airplane needs to develop a customized, scheduled maintenance and inspection program.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Task',
        label='Task',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRO.Aviation:Workstation',
        label='Workstation',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Disposet',
        label='Disposet',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Manufacturer',
        label='Manufacturer',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Measure',
        label='Measure',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:NormItem',
        label='NormItem',
        description='an MRP relevant definition of a norm',
        valid='start=2019-02-18;',
        created_by='Christian Schulz',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:PSG',
        label='PSG',
        description='Planung Sachgebiet which contains  disposets.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Part',
        label='Part',
        description='a part or material',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Store',
        label='Store',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Threshold',
        label='Threshold',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Vorgang',
        label='Vorgang',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.MRP:Workshop',
        label='Workshop',
        description='TODO.',
        valid='start=2018-09-07;',
        created_by='Kaushik',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:AppInstance',
        label='AppInstance',
        description='Mobile application instance.',
        valid='start=2020-03-15;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:DeviceSpecifications',
        label='DeviceSpecifications',
        description='Mobile device specifications i.e. model, manufacturer ...',
        valid='start=2020-03-15;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:Encounter',
        label='Encounter',
        description='Defined connection between applications.',
        valid='start=2020-03-15;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:HealthInfo',
        label='HealthInfo',
        description='information regarding app instance.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:LicenceCodes',
        label='LicenceCodes',
        description='Unique Licence Codes which is used for mobile app activation.',
        valid='start=2020-07-09;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:Message',
        label='Message',
        description='Message nodes created when new messages are available for App.',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Mobile:MsgTemplate',
        label='MsgTemplate',
        description='Message templates in different languages.',
        valid='start=2020-04-07;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:AccessControlList',
        label='AccessControlList',
        description='An access control list (ACL), with respect to a computer file system, is a list of permissions attached to an object. An ACL specifies which users or system processes are granted access to objects, as well as what operations are allowed on given objects.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:FCHBA',
        label='FCHBA',
        description='Fibre Channel Host Bus Adapter, Physical/Virtual Circuit allowing an endpoint to connect to a network.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:IDSIPS',
        label='IDSIPS',
        description='Intrution Detection and Intrusion Prevention System are network security appliances that monitor network and/or system activities for malicious activity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:IPAddress',
        label='IPAddress',
        description='A Network IPAddress is per network unique identifier for IP-Devices.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Loadbalancer',
        label='Loadbalancer',
        description='A Loadbaancer distributes network loads between multiple endpoints/hosts.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:MACAddress',
        label='MACAddress',
        description='MAC-Adress is a globally unique identifier for Ethernet Adapters',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NIC',
        label='NIC',
        description='NIC, or Network Interface Card is a Physical/Virtual Circuit allowing an endpoint to connect to a network.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkCard',
        label='NetworkCard',
        description='Physical Networking Module to be fitted into an enclosure.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkElement',
        label='NetworkElement',
        description='A Network Element represents a manageable entity in a network. either a single physical device or a group of devices.',
        valid='start=2020-09-04;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkEnclosure',
        label='NetworkEnclosure',
        description='Networking Enclosure is a physical Entity hosing Physical Networking Devices',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkEndpoint',
        label='NetworkEndpoint',
        description='An endpoint device is an Internet-capable computer hardware device on a TCP/IP network. The term can refer to desktop computers, laptops, smart phones, tablets, thin clients, printers or other specialized hardware such POS terminals and smart meters.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkFabric',
        label='NetworkFabric',
        description='Networking Fabric is a virtual/physical Entity housing Networking Devices',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkFilter',
        label='NetworkFilter',
        description='A Network Filter is a security measure restricting usage.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkInterface',
        label='NetworkInterface',
        description='Logical or physical network interface.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkLink',
        label='NetworkLink',
        description='A Network Link represents a logical connection between interfaces, elements, or sites.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:NetworkSetting',
        label='NetworkSetting',
        description='Network Policy is a generic definition that outlines rules for computer network access, determines how policies are enforced and lays out some of the basic architecture of the company security/ network security environment.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Port',
        label='Port',
        description='A physical or logical network port',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:PortChannel',
        label='PortChannel',
        description='A Portchannel bundles two or more physical or logical network ports',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Router',
        label='Router',
        description='Networking Device for forwarding data packet between networks',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Shelf',
        label='Shelf',
        description='Shelf is a physical entity inside a enclosure, each enclosure can house one to many shelfs',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:SimpleDevice',
        label='SimpleDevice',
        description='Standalone networking device, which could be physical or virtual',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Site',
        label='Site',
        description='A site located in on place, which contains a  geographically concentrated computer network.',
        valid='start=2020-09-04;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Slot',
        label='Slot',
        description='Slot is a physical entity inside a shelf allowing to plug in extension moduls, e. g. network interface moduls oder CPU modules.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Subnet',
        label='Subnet',
        description='Subnet is a group of IDAddresses located in one place.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:Switch',
        label='Switch',
        description='Networking device for packet switching',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:VLAN',
        label='VLAN',
        description='VLAN or Virtual LAN is a group of computers or network devices that appear to be on the same LAN, even if they are distributed. VLANs allow segregation of traffic within a network.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Network:WifiAccessPoint',
        label='WifiAccessPoint',
        description='Device offering wireless/radio networking services',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Node',
        label='Node',
        description='The root node, the \'Big Bang\'. The nodes Global, Factual, Actionable and Situational build with this Node the\ntop level of the SGO.',
        valid='start=2013-11-01;',
        hide=True,
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Note',
        label='Note',
        description='Any type of note.',
        valid='start=2015-04-29;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Notification',
        label='Notification',
        description='A notification event',
        valid='start=2015-04-27;',
        created_by='cwalker@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-arch:LinkType',
        label='Link Type',
        description='A locally managed resource that describes a link type predicate that might otherwise not be directly resolvable.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-arch:Resource',
        label='Architecture Resource',
        description='A generic architecture resource.  A resource of this type is likely to be a model or design artifact.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-asset:Artifact',
        label='Artifact',
        description='The Artifact fragment',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-asset:Asset',
        label='Asset',
        description='The Asset resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-automation:AutomationPlan',
        label='AutomationPlan',
        description='The Automation Plan resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-automation:AutomationRequest',
        label='AutomationRequest',
        description='The Automation Request resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-automation:AutomationResult',
        label='AutomationResult',
        description='The Automation Result resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-automation:ParameterInstance',
        label='ParameterInstance',
        description='The Automation Parameter Instance resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-automation:TeardownAction',
        label='TeardownAction',
        description='An action that tears down a previously deployed resource. It is likely that the resource was deployed using an OSLC Automation deployment plan, but this is not always the case. That is, a tear-down action typically has the opposite semantics from a oslc_auto:Deploy sub-domain Automation Plan or Request, even if the service provider offers no equivalents in its Automation Plan collection.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-change:ChangeRequest',
        label='ChangeRequest',
        description='The CM Change Request resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:AllowedValues',
        label='AllowedValues',
        description='Allowed values for one property.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Comment',
        label='Comment',
        description='A Comment resource represents a single note, or comment, in a discussion thread.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Compact',
        label='Compact',
        description='The Compact representation, fetched as application/x-oslc-compact+xml',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:CreationFactory',
        label='CreationFactory',
        description='The CreationFactory definition included in a ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Dialog',
        label='Dialog',
        description='The Dialog definition included in ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Discussion',
        label='Discussion',
        description='A Discussion resource is intended to represent a sequence of comments or notes regarding the associated resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Error',
        label='Error',
        description='Basis for forming an error response.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:ExtendedError',
        label='ExtendedError',
        description='Extended error information.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:OAuthConfiguration',
        label='OAuthConfiguration',
        description='The OAuthConfiguration definition included in ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:PrefixDefinition',
        label='PrefixDefinition',
        description='The PrefixDefinition definition included in ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Preview',
        label='Preview',
        description='The UI Preview representation.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Property',
        label='Property',
        description='A Property resource describes one allowed or required property of a resource.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Publisher',
        label='Publisher',
        description='The Publisher definition included in ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:QueryCapability',
        label='QueryCapability',
        description='The QueryCapability definition included in a ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:ResourceShape',
        label='ResourceShape',
        description='The Resource Shape used for creation, query and modify.  Formally, a shape S applies to a resource R if there is a triple R rdf:type T and there is a triple S oslc:describes T, or if there is a triple R oslc:instanceShape S.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:ResponseInfo',
        label='ResponseInfo',
        description='The ResponseInfo included in query results.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:Service',
        label='Service',
        description='The Service definition included in a ServiceProvider.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:ServiceProvider',
        label='ServiceProvider',
        description='The Service Provider resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-core:ServiceProviderCatalog',
        label='ServiceProviderCatalog',
        description='The Service Provider Catalog resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:ComputerSystem',
        label='ComputerSystem',
        description='An intelligent device, such as a computer, that can perform computing, data collection, and/or communication operations. This category includes general purpose computers, such as laptops, servers, and virtual machines; computers with specific functions, such as Networking and Storage hardware, Voice over IP Telephony devices, HVAC systems; monitoring data collection devices in buildings, automobiles, or electronic grids.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:Database',
        label='Database',
        description='An organized collection of digital data that is managed by a database management system (DBMS). (A Database Management System, in turn, is represented as a SoftwareServer).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:IPAddress',
        label='IPAddress',
        description='Represents an IP address, either IPv4-based or IPv6-based.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:OperatingSystem',
        label='OperatingSystem',
        description='Represents the operating system or control software installed and running on a ComputerSystem',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:Path',
        label='Path',
        description='Path represents individual components of a directed graph of resources, where specific ordering is necessary to preserve a graph. Examples of such directed graphs are the representation of workflows or processes.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:Process',
        label='Process',
        description='This resource represents a process running under an operating system.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:ServerAccessPoint',
        label='ServerAccessPoint',
        description='A network endpoint, i.e. the combination of IP address and port number that clients connect to when accessing a SoftwareServer.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:ServiceInstance',
        label='ServiceInstance',
        description='A Service Instance is the representation of a service offering that was selected by the customer and then instantiated for that specific customer. Service Instances are supported by definite and measurable warranties or guarantees that the expected level of service/value will be met. Instances of the resource carry exposure from the group that is responsible for supporting the offering externally to the group that is utilizing the offering. It is common to group or nest instances together to form a service instance hierarchy. This resource definition does not represent the individual processes and/or activities that comprise an overall service except in the case where such processes are viewed as an independent service. In this condition, an instance of ServiceInstance would be created to represent the ServiceInstance of the process, then creating a hierarchy of ServiceInstances (to the containing ServiceInstance).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:SoftwareModule',
        label='SoftwareModule',
        description='Represents packaged components that are deployed to a SoftwareServer.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:SoftwareServer',
        label='SoftwareServer',
        description='Represents an instance of software that participates in hosting a particular application.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:StorageVolume',
        label='StorageVolume',
        description='Represents an identifiable unit of data storage. A StorageVolume can be a physical device ( e.g. a removable hard drive ) or a logical unit created by combining one or more other storage volumes.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-crtv:Tablespace',
        label='Tablespace',
        description='the storage area used by an Database to store its data. Database administrators define how Tablespaces maps to actual system storage. A Tablespace can be a physical device ( e.g. a removable hard drive ) or a logical unit (e.g. a file or a virtual disk).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Baseline',
        label='Baseline',
        description='\nA baseline is a set of estimates, based on some scenario, that are used to track the performance of a project.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:BaselineList',
        label='BaselineList',
        description='A baseline list is a container for baseline resources.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:CdfPoint',
        label='CdfPoint',
        description='\n<p>This class describes a point on the graph of a cumulative probability function.\nThe cumulative probability at a point is given by\n<a href=\"#probability\"><code>ems:probability</code></a>.\nThe cumulative probability MUST be greater than 0 and less than 1.\nThe measurement value is given by\n<a href=\"#numericValue\"><code>ems:numericValue</code></a>.\n<p>The probability that a measurement gives a value less than or equal to\nthe numeric value is equal to the cumulative probability.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:CumulativeDistributionFunction',
        label='CumulativeDistributionFunction',
        description='\n<p>A <em>cumulative distribution function</em> (cdf) is a probabilty distribution defined by giving the\ncumulative probability at an increasing sequence of measurement values.\nThe range of possible measurement values may be unbounded.\nIf a lower bound exists, it is given by <a href=\"#low\"><code>ems:low</code></a>.\nIf an upper bound exists, it is given by <a href=\"#high\"><code>ems:high</code></a>.</p>\n\n<p>The graph of the cumulative distribution function is given by a set of measurement values\nat an increasing sequence of cumulative probabilities between 0 and 1.\nThe cumulative probability values are given by one or more\n<a href=\"#cdfPoint\"><code>ems:cdfPoint</code></a> properties.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Dimension',
        label='Dimension',
        description='\nA <em>dimension</em> is some aspect of an aggregated quantity which lets the aggregate be analyzed.\nFor example, the total effort expended in a project can be analyzed by week or month.\nTherefore time\n(<a href=\"http://open-services.net/ns/ems/dimension#Time\"><code>dimension:Time</code></a>)\nis a dimension of effort\n(<a href=\"http://open-services.net/ns/ems/metric#Effort\"><code>metric:Effort</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:DimensionCell',
        label='DimensionCell',
        description='\nThis class describes a dimension cell in a row of a fact table.\nA dimension cell refers to its column\n(see <a href=\"#ems:inColumn\"><code>ems:inColumn</code></a>\nand has a dimension member\n(see <a href=\"#dimensionMember\"><code>ems:dimensionMember</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:DimensionColumn',
        label='DimensionColumn',
        description='\nThis class describes a dimension column in a fact table.\nA dimension column has a dimension\n(see <a href=\"#dimension\"><code>ems:dimension</code>) and grain\n(see <a href=\"#grain\"><code>ems:grain</code></a> and may refer to a map\n(see <a href=\"#useMap\"><code>ems:useMap</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:DimensionMember',
        label='DimensionMember',
        description='\nA <em>dimension member</em> is some subset of a dimension.\nFor example, work on a project is performed by people in various roles.\nIt is often of interest to break down an effort estimate or measurement by role.\nMembers of the dimension <em>role</em>\n(<a href=\"http://open-services.net/ns/ems/dimension#Role\"><code>dimension:Role</code></a>)\ninclude <em>manager</em>\n(<a href=\"http://open-services.net/ns/ems/dimension-member#Manager\"><code>dimension-member:Manager</code></a>\nand <em>programmer</em>\n(<a href=\"http://open-services.net/ns/ems/dimension-member#Programmer\"><code>dimension-member:Programmer</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:EffortMetric',
        label='EffortMetric',
        description='\nAn <em>effort metric</em> is a metric that measures the effort of effort required to perform some task.\nFor example,\n<em>effort</em> as measured in person-months, person-years, etc.\n(<a href=\"http://open-services.net/ns/ems/metric#Effort\"><code>metric:Effort</code></a>),\n<em>average staffing</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Staffing\"><code>metric:Staffing</code></a>),\n<em>peak staffing</em>\n(<a href=\"http://open-services.net/ns/ems/metric#PeakStaffing\"><code>metric:PeakStaffing</code></a>), and\n<em>full-time equivalents</em>\n(<a href=\"http://open-services.net/ns/ems/metric#FullTimeEquivalent\"><code>metric:FullTimeEquivalent</code></a>)\nare effort metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Estimate',
        label='Estimate',
        description='An estimate is a probabilistic prediction, based on a scenario, for a set of measurements.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:EstimateList',
        label='EstimateList',
        description='An estimate list is a container for estimate resources.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Fact',
        label='Fact',
        description='\nThis class describes a row of a fact table\n(see <a href=\"#FactTable\"><code>ems:FactTable</code></a>).\nEach fact row has a set of dimension cells\n(see <a href=\"#DimensionCell\"><code>ems:DimensionCell</code></a>)\nand measure cells\n(see <a href=\"#MeasureCell\">ems:MeasureCell</a>).\nThese MUST match the description of the columns given in the head of the fact table\n(see <a href=\"#Head\"><code>ems:Head</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:FactDistribution',
        label='FactDistribution',
        description='\nA <em>fact distribution</em> is a row of a fact distribution table\n(see <a href=\"#FactDistributionTable\"><code>ems:FactDistributionTable</code></a>).\nIt contains one or more dimension cells\n(see <a href=\"#dimensionCell\"><code>ems:dimensionCell</code></a>) and one or more measure distribution cells\n(see <a href=\"#measureDistributionCell\"><code>ems:measureDistributionCell</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:FactDistributionTable',
        label='FactDistributionTable',
        description='\n<p>A <em>fact distribution table</em> is a fact table that contains probability distributions\ninstead of precise numeric values for its measures.\nFact distribution tables are used in scenario assumptions\n(see <a href=\"#assumesTable\"><code>ems:assumesTable</code></a>) and estimate predictions\n(see <a href=\"#predictsTable\"><code>ems:predictsTable</code></a>).</p>\n\n<p>A fact distribution table is similar to a fact table\n(see <a href=\"#FactTable\"><code>ems:FactTable</code></a>),\nexcept that it has <em>fact distribution</em> rows\n(see <a href=\"#FactDistribution\"><code>ems:FactDistribution</code></a>) instead of fact rows\n(see <a href=\"#Fact\"><code>ems:Fact</code></a>), and they have <em>measure distribution</em> cells\n(see <a href=\"#MeasureDistributionCell\"><code>ems:MeasureDistributionCell</code></a>) instead of measure cells\n(see <a href=\"#MeasureCell\"><code>ems:MeasureCell</code></a>).</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:FactTable',
        label='FactTable',
        description='\n<p>This class is used to represent <em>fact tables</em>.</p>\n\n<p>Consider the work performed on a project.\nWork may be analyzed according to attributes such as who performed the work,\nthe task or activity that the work accomplished,\nwhen the work was performed, etc.\nThese attributes are referred to as <em>dimensions</em>.</p>\n\n<p>Work may be quantified by such metrics as its effort in person-hours,\nits cost in some currency, its duration in months, its peak staffing, etc.\nThese quantities are referred to as <em>measures</em>.</p>\n\n<p>The term dimension is used because the measures can be regarded as occupying cells\nin a multi-dimensional array (sometimes referred to as a <em>datacube</em>).\nIt is frequently of interest to summarize the measures along a dimension,\nfor example given the effort by activity, calculate the total effort for all activities.\nConversely, given the total effort, it may be of interest to see how it is broken down by activity.</p>\n\n<p>In general, set of related measures, analyzed along a set of dimensions may be organized into a\n<a href=\"http://en.wikipedia.org/wiki/Fact_table\">fact table</a>.\nEach row of a fact table contains a set of measures (e.g. effort and cost)\nfor a given combination of dimension values (e.g. activity and month).</p>\n\n<p>This resource MAY contain the actual measurements,\nprovide a link to the source of the actual measurements,\nor contain both a link to the source and a copy of the actual measurements obtained from the source\n(i.e. a cached copy of the source).</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:FinancialMetric',
        label='FinancialMetric',
        description='\nA <em>financial metric</em> is a metric that measures the cost of an artifact or work effort.\nFor example,\n<em>total cost</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Cost\"><code>metric:Cost</code></a>) and\n<em>labor cost</em>\n(<a href=\"http://open-services.net/ns/ems/metric#LaborCost\"><code>metric:LaborCost</code></a>)\nare financial metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Format',
        label='Format',
        description='\nA <em>format</em> is a specification of the syntax of an artifact.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Grain',
        label='Grain',
        description='\nDimensions may be aggregated into subsets of various sizes.\nA <em>grain</em> is a unit of aggregation of a dimension.\nFor example, <em>month</em>\n(<a href=\"http://open-services.net/ns/ems/grain#CalendarMonth\"><code>grain:CalendarMonth</code></a>) and <em>week</em>\n(<a href=\"http://open-services.net/ns/ems/grain#CalendarWeek\"><code>grain:CalendarWeek</code></a>) are grain sizes for the dimension <em>time</em>\n(<a href=\"http://open-services.net/ns/ems/dimension#Time\"><code>dimension:Time</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Head',
        label='Head',
        description='\nThis class defined the columns of a fact table.\nA fact table MUST have one or more dimension columns, e.g. date or role,\nand one or more measure columns, e.g. cost or effort.\nThe dimension columns contain dimension values.\nDimension columns SHOULD contain standard dimension values when they exist, e.g. for roles.\nThe creator of the fact table MAY use custom dimension dimension values and\nrecord how these custom values are mapped to the standard values.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Map',
        label='Map',
        description='\n<p>Some key dimensions may define standard dimension member URIs which are used for\ndata interchange. However, users may wish to use custom values.\nThis class lets you define how custom values are mapped to standard URIs.\nYou can include an map resource in the description of a dimension column of a fact table\n(see <a href=\"#useMap\"><code>ems:useMap</code></a>).</p>\n\n<p>We make the simplifying assumption that this mapping is many-to-one, that is,\none or more custom dimension values may be mapped to the same standard dimension value.\nA map may contain one or more of these mappings\n(see <a href=\"#mapping\"><code>ems:mapping</code></a>), but each custom dimension value must map to\nexactly one standard dimension value.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Mapping',
        label='Mapping',
        description='\nThis class describes a <em>mapping</em>.\nA mapping maps some custom string label value for a dimension\n(see <a href=\"#from\"><code>ems:from</code></a>) to a dimension member URI which may be a standard\nvalue defined in some vocabulary.\n(see <a href=\"#to\"><code>ems:to</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Measure',
        label='Measure',
        description='\nA <em>measure</em>, as in the idiom <em>take the measure of</em>,\nis the result of observing some numerically quantifiable aspect of a project, system, or thing.\nFor example, a <em>duration of 12 months</em> or a <em>size of 10 KLOC</em> are measures.\nThe aspect being measured, e.g. duration or size, is referred to as the <em>metric</em>\nand is given by the property <a href=\'#metric\'><code>ems:metric</code></a>.\nThe scale of measurement, e.g. months or KLOC, is referred to as the <em>unit of measure</em>\nand is given by the property <a href=\"#unitOfMeasure\"><code>ems:unitOfMeasure</code></a>.\nThe numeric value of an observation, e.g. 12 or 10, is given by the property\n<a href=\"numericValue\"><code>ems:numericValue</a></code>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:MeasureCell',
        label='MeasureCell',
        description='\nThis class descibes measure cells.\nA measure cell refers to a measure column\n(see <a href=\"#inColumn\"><code>ems:inColumn</code></a>)\nand has a numeric value\n(see <a href=\"numericValue\"><code>ems:numericValue</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:MeasureColumn',
        label='MeasureColumn',
        description='\nThis class describes a measure column of a fact table.\nA measure column has a metric\n(see <a href=\"#metric\"><code>ems:metric</code></a>\nand a unit of measure\n(see <a href=\"#unitOfMeasure\"><code>ems:unitOfMeasure</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:MeasureDistribution',
        label='MeasureDistribution',
        description='\nA <em>measure distribution</em> is like a measure\n(see <a href=\"#Measure\"><code>ems:Measure</code></a>)\nexcept that it gives a probability distribution for the numeric value of a measure instead of a precise numeric value.\nMeasure distributions are used in scenario assumptions\n(see <a href=\"#assumes\"><code>ems:assumes</code></a> and\n<a href=\"#assumesTable\"><code>ems:assumesTable</code></a>) and\nestimate predications\n(see <a href=\"#predicts\"><code>ems:predicts</code></a> and\n<a href=\"#predictsTable\"><code>ems:predictsTable</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:MeasureDistributionCell',
        label='MeasureDistributionCell',
        description='\nA <em>measure distribution cell</em> is a cell in a fact distribution row.\nIt refers to its column\n(see <a href=\"#inColumn\"><code>ems:inColumn</code></a>) and contains a measure distribution\n(see <a href=\"#distribution\"><code>ems:distribution</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Measurement',
        label='Measurement',
        description='A measurement is a set of observations of numerically quantifiable aspects of a project, system, or thing.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:MeasurementList',
        label='MeasurementList',
        description='A measurement list is a container for measurement resources.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Metric',
        label='Metric',
        description='\nA <em>metric</em> is a procedure or algorithm for quantifying or measuring some aspect of a thing, system, event, etc.\nFor example <em>duration</em> is a metric that measures the amount of time an activity takes.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:NormalDistribution',
        label='NormalDistribution',
        description='\nA <em>normal distribution</em> (also known as a <em>Gaussian distribution</em>\nis a probability distribution that naturally arises as the\nlimit of many random factors. It is symmetric about its mean and has a certain scale.\nThe mean is given by <a href=\"#mu\"><code>ems:mu</code></a>.\nIts scale (also known as its standard deviation) is given by\n<a href=\"#scale\"><code>ems:scale</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:PointEstimate',
        label='PointEstimate',
        description='\nA <em>point estimate</em> is a probability distribution that is concentrated at a single value.\nThe single value is given by <a href=\"#numericValue\"><code>ems:numericValue</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:PoissonDistribution',
        label='PoissonDistribution',
        description='\nA <em>Poisson distribution</em> is a probability distribution that gives the probability\nthat a given number of events will occur in a fixed time period.\nThis distribution is completely specified by a single parameter often denoted by the\nGreek letter <em>lambda</em>.\nLambda is given by <a href=\"#lambda\"><code>ems:lambda</code>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ProbabilityDistribution',
        label='ProbabilityDistribution',
        description='\nThis class describes <em>probability distributions</em>.\nA probability distribution gives the likelihood that a measurement of some value\n(a random variable)\nwill fall within some given range.\nProbability distributions are used in scenario assumptions\n(see <a href=\"#assumes\"><code>ems:assumes</code></a>) and estimate predictions\n(see <a href=\"#predicts\"><code>ems:predicts</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ProcessMetric',
        label='ProcessMetric',
        description='\nA <em>process metric</em> is a metric that measures the process used to create an artifact such as software.\nFor example,\n<em>build</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Builds\"><code>metric:Builds</code></a>) and\n<em>test executions</em>\n(<a href=\"http://open-services.net/ns/ems/metric#TestExecutions\"><code>metric:TestExecutions</code></a>)\nare process metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ProductivityMetric',
        label='ProductivityMetric',
        description='\nA <em>productivity metric</em> is a metric that measures the rate at which some artifact, such as software, is produced.\nFor example,\n<em>lines of code per unit time</em>\n(<a href=\"http://open-services.net/ns/ems/metric#EslocPerTime\"><code>metric:EslocPerTime</code></a>) and\n<em>team velocity</em>\n(<a href=\"http://open-services.net/ns/ems/metric#TeamVelocity\"><code>metric:TeamVelocity</code></a>)\nare productivity metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Project',
        label='Project',
        description='Within the scope of EMS, a project is any activity, system, or thing that can be the subject of a set of measurements.\nIn practice, a project is often a time-bounded work effort that produces a unique result.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ProjectList',
        label='ProjectList',
        description='A project list is a container for projects.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Quantile',
        label='Quantile',
        description='\n<p>This class describes a <em>quantile</em> of a quantile function.\nThe cumulative probability of a quantile is given by\n<a href=\"#probability\"><code>ems:probability</code></a>.\nThe cumulative probability MUST be greater than 0 and less than 1.\nThe upper limit of the range of measurement values is given by\n<a href=\"#numericValue\"><code>ems:numericValue</code></a>.\nThe lower limit of the range of measurement values is given by\nthe upper limit of the preceding quantiles.</p>\n<p>The probability that a measurement gives a value less than or equal to\nthe numeric value is equal to the cumulative probability.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:QuantileFunction',
        label='QuantileDistribution',
        description='\n<p>A <em>quantile function</em> is a probability distribution that breaks up a range of values\ninto quantiles that each have the same probability.\nWhen the number of quantiles is 4, 10, or 100, we refer to them as <em>quartiles</em>,\n<em>deciles</em>, and <em>percentiles</em>.\nFor example, there is a 25% probability that a measurement will fall within any given quartile.\nThe number of quantiles is given by\n<a href=\"#numberOfQuantiles\"><code>ems:numberOfQuantiles</code></a>.\nThe number of quantiles MUST be greater than one.</p>\n\n<p>The range of possible measurement values may be unbounded.\nIf a lower bound exists, it is given by <a href=\"#low\"><code>ems:low</code></a>.\nIf an upper bound exists, it is given by <a href=\"#high\"><code>ems:high</code></a>.</p>\n\n<p>The graph of the quantile function is given by a set of measurement values that\ncorrespond to the equally spaced cumulative probabilities between 0 and 1.\nFor example, for quartiles the cumulative probabilities are 25%, 50%, and 75%.\nThe cumulative probability values are given by one or more\n<a href=\"#quantile\"><code>ems:quantile</code></a> properties.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ReliabilityMetric',
        label='ReliabilityMetric',
        description='\nA <em>reliability metric</em> is a metric that measures the correctness or absence of failures in a system such as a software system.\nFor example\n<em>defects</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Defects\"><code>metric:Defects</code></a>),\n<em>failures</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Failures\"><code>metric:Failures</code></a>), and\n<em>mean time to failure</em>\n(<a href=\"http://open-services.net/ns/ems/metric#MeanTimeToFailure\"><code>metric:MeanTimeToFailure</code></a>)\nare reliability metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Scenario',
        label='Scenario',
        description='\nA scenario is a set of assumptions about how a project will be executed.\nThese assumptions are used as inputs to estimates.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:ScenarioList',
        label='ScenarioList',
        description='A scenario list is a container for scenario resources.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:Service',
        label='Service',
        description='\nAn EMS <em>service</em> hosts and manages a set of resources that describe projects, scenarios, estimates, measurements, and baselines.\nEach instance of an service has a set of resource containers that contain resources of a given type.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:SizeMetric',
        label='SizeMetric',
        description='\nA <em>size metric</em> is a metric that measures the magnitude, volume, bulk, or capability of some artifact such as software.\nFor example,\n<em>lines of code</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Sloc\"><code>metric:Sloc</code></a>) and\n<em>story points</em>\n(<a href=\"http://open-services.net/ns/ems/metric#StoryPoints\"><code>metric:StoryPoints</code></a>)\nare size metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:TimeMetric',
        label='TimeMetric',
        description='\nA <em>time metric</em> is a metric that describes some temporal aspect of a project, system, or thing.\nFor example,\n<em>duration</em> (<a href=\"http://open-services.net/ns/ems/metric#Duration\"><code>metric:Duration</code></a>),\n<em>start</em> (<a href=\"http://open-services.net/ns/ems/metric#Start\"><code>metric:Start</code></a>), and\n<em>finish</em> (<a href=\"http://open-services.net/ns/ems/metric#Finish\"><code>metric:Finish</code></a>) are time metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:TriangularDistribution',
        label='TriangularDistribution',
        description='\nA <em>triangular distribution</em> is a probability distribution that concentrated between\n<em>high</em> and <em>low</em> values, and that linearly rises to and falls from to an\nintermediate <em>most likely</em> value.\nThe low value is given by <a href=\"#low\"><code>ems:low</code></a>.\nThe most likely value is given by <a href=\"#mostLikely\"><code>ems:mostLikely</code></a>.\nThe high value is given by <a href=\"#high\"><code>ems:high</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:UniformDistribution',
        label='UniformDistribution',
        description='\nA <em>uniform distribution</em> is a probability distribution that is evenly spread between\na <em>high</em> and a <em>low</em> value.\nThe high value is given by <a href=\"#high\"><code>ems:high</code></a>.\nThe low value is given by <a href=\"#low\"><code>ems:low</code></a>.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:UnitOfMeasure',
        label='UnitOfMeasure',
        description='\nA <em>unit of measure</em> specifies a procedure for associating a numeric value with some metric.\nFor example, <em>month</em>\n(<a href=\"http://open-services.net/ns/ems/unit#Month\"><code>unit:Month</code></a>)\nis a unit of measure for <em>duration</em>\n(<a href=\"http://open-services.net/ns/ems/metric#Duration\"><code>metric:Duration</code></a>).',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:WbsFormat',
        label='WbsFormat',
        description='\nA <em>WBS format</em> is a format that specifies the syntax of work breakdown structures.\nFor example,\n<a href=\"http://schemas.microsoft.com/project/2007\"><code>http://schemas.microsoft.com/project/2007</code></a>\nis the format for\nMicrosoft Office Project 2007 XML Data Interchange Schema.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-ems:WorkBreakdownStructure',
        label='WorkBreakdownStructure',
        description='\n<p>This class describes <em>work breakdown structures</em>.\nA <a href=\"http://en.wikipedia.org/wiki/Work_breakdown_structure\">work breakdown structure</a> (WBS) is a common way to represent the work to be performed in a project.\nIn EMS, a WBS may be used as an assumption in an scenario,\nas a prediction in an estimate, or as an observation in a measurement.</p>\n\n<p>A WBS has a format\n(see <a href=\"#wbsFormat\"><code>ems:wbsFormat</code></a>), and may either include\n(see <a href=\"#wbsContent\"><code>ems:wbsContent</code></a>) or link to\n(see <a href=\"#wbsSource\"><code>ems:wbsSource</code></a>) its content.\nThe included or linked WBS content MUST be in the specified format.</p>',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:AvgJmsGetTime',
        label='AvgJmsGetTime',
        description='Average time required for a system to respond to a Java Messaging Service GET request',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:AvgLoginRequestFailures',
        label='AvgLoginRequestFailures',
        description='Average login request failures',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:AvgRequestFailures',
        label='AvgRequestFailures',
        description='Average request failures',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:BufferPoolHits',
        label='BufferPoolHits',
        description='Buffer pool hits, e.g. hit ratio or count',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:BufferPoolMetrics',
        label='BufferPoolMetrics',
        description='Metric category for buffer pool-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:CpuMetrics',
        label='CpuMetrics',
        description='Metric category for CPU-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:CpuSpeed',
        label='CpuSpeed',
        description='Speed of the CPU',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:CpuUsed',
        label='CpuUsed',
        description='CPU used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:DiskMetrics',
        label='DiskMetrics',
        description='Metric category for disk-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:DiskSpaceOverCommitAmount',
        label='DiskSpaceOverCommitAmount',
        description='Amount of disk space committed beyond the disk\'s capacity.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:DiskSpaceUsed',
        label='DiskSpaceUsed',
        description='Disk space used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:FailureMetrics',
        label='FailureMetrics',
        description='Metric category for requests that fail.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:GarbageCollectionRequests',
        label='GarbageCollectionRequests',
        description='Garbage collection requests',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:HeapMemoryUsed',
        label='HeapMemoryUsed',
        description='Heap memory used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:HighDepthQueueCount',
        label='HighDepthQueueCount',
        description='TODO',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:HostedDatabases',
        label='HostedDatabases',
        description='Databases hosted, either absolute or relative to some maximum',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:LocalInboundConnections',
        label='LocalInboundConnections',
        description='Local inbound connections',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:LockListUsed',
        label='LockListUsed',
        description='Lock usage',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:LogUsed',
        label='LogUsed',
        description='Amount of log used, either absolute or relative to some maximum',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:LoginRequestFailures',
        label='LoginRequestFailures',
        description='Failed login requests',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:MemoryAvailableAfterGarbageCollection',
        label='MemoryAvailableAfterGarbageCollection',
        description='Memory available following completion of a garbage collection request.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:MemoryMetrics',
        label='MemoryMetrics',
        description='Metric category for memory-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:MessageCount',
        label='MessageCount',
        description='TODO',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:Metric',
        label='Metric',
        description='Metric category for metrics defined in the Performance Monitoring vocabulary.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:NetworkIOErrors',
        label='NetworkIOErrors',
        description='Network packets sent or received that did not complete successfully.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:NetworkMetrics',
        label='NetworkMetrics',
        description='Metric category for network-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:PerMinute',
        label='PerMinute',
        description='Units for a quantity where a value of one represents 60 seconds of time.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:PerformanceMonitoringRecord',
        label='PerformanceMonitoringRecord',
        description='A resource representing performance monitoring information',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:QueueDepth',
        label='QueueDepth',
        description='Size/lenght/depth of a queue',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:QueueFull',
        label='QueueFull',
        description='A queue filled to its maximum capacity',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:RealMemoryUsed',
        label='RealMemoryUsed',
        description='Real memory used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:RemoteInboundConnections',
        label='RemoteInboundConnections',
        description='Remote inbound connections',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:RequestFailures',
        label='RequestFailures',
        description='Request failures',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:RequestMetrics',
        label='RequestMetrics',
        description='Metric category for requests on a resource, originating from an end user or a system component.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceAvailabilityMetrics',
        label='ResourceAvailabilityMetrics',
        description='Metric category for metrics that show resource availability.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceExhaustionMetrics',
        label='ResourceExhaustionMetrics',
        description='Metric category for metrics that show resource consumption in excess of capacity.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceUsageMetrics',
        label='ResourceUsageMetrics',
        description='Metric category for metrics that show resource usage.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ResponseTime',
        label='ResponseTime',
        description='Time required for some system to respond to a request',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ResponseTimeMetrics',
        label='ResponseTimeMetrics',
        description='Metric category for metrics that show time it takes for a response to be returned to a request.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:SortOverflows',
        label='SortOverflows',
        description='A sort\'s performance was impacted because the data to be sorted is large enough for it to overflow from (relatively) fast to (relatively) slow storage.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:SqlStatmentFailures',
        label='SqlStatmentFailures',
        description='SQL statements that failed',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:TableSpaceFree',
        label='TableSpaceFree',
        description='Table space free.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:TableSpaceUsed',
        label='TableSpaceUsed',
        description='Table space used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:ThreadPoolMetrics',
        label='ThreadPoolMetrics',
        description='Metric category for thread pool-related metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:TimeDatabaseThreadPoolExhausted',
        label='TimeDatabaseThreadPoolExhausted',
        description='TODO',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:TimeJCAThreadPoolExhausted',
        label='TimeJCAThreadPoolExhausted',
        description='Time during which a Java Connection Architecture thread pool was fully utilized (no threads were free)',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:TimeThreadPoolExhausted',
        label='TimeThreadPoolExhausted',
        description='Time during which a thread pool was fully utilized (no threads were free)',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:VirtualMemoryUsed',
        label='VirtualMemoryUsed',
        description='Virtual memory used.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:VirtualizationMetrics',
        label='VirtualizationMetrics',
        description='Metric category for virtualization-related resource metrics.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-perfmon:VmCpuReady',
        label='VmCpuReady',
        description='Amount of CPU ready from a virtual machine\'s point of view',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-qm:TestCase',
        label='TestCase',
        description='The QM Test Case resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-qm:TestExecutionRecord',
        label='TestExecutionRecord',
        description='The QM Test Execution Record resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-qm:TestPlan',
        label='TestPlan',
        description='The QM Test Plan resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-qm:TestResult',
        label='TestResult',
        description='The QM Test Result resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-qm:TestScript',
        label='TestScript',
        description='The QM Test Script resource',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-reqman:Requirement',
        label='Requirement',
        description='Statement of\n            need.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.OSLC-reqman:RequirementCollection',
        label='RequirementCollection',
        description='Collection of requirements. A\n            collection uses zero or more requirements.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:OntologyAttribute',
        label='OntologyAttribute',
        description='represents any Attribute definition from OGIT',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:OntologyEntity',
        label='OntologyEntity',
        description='represents any Entity definition from OGIT\nwhenever there is a Schema describing/restricting the entity\'s content there will be \"isUsedBy\" link from Schema to OntologyEntity',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:OntologyVerb',
        label='OntologyVerb',
        description='represents any Verb definition from OGIT',
        valid='start=2015-05-21;',
        hide=True,
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Organization',
        label='Organization',
        description='An identity that represents an organization, company, or some other grouping of Person objects.\nEntities of this type should be created with a predefined ID. Those IDs should be named like a domain name, i.e.\na concatention of some strings separated with a dot. if organization data is created from a LDAP then a mapping\nlike \"cn=John Doe,dc=example,dc=com\" => \"john_doe.example.com\" should be employed.\nThe ogit/function attribute should be used to tell what kind of grouping an entity of type Organization is: company, department, group, ...',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.PTF:Dummy',
        label='Dummy',
        description='Only for containing dummy variables during the performance tests.',
        valid='start=2019-01-29;',
        created_by='TGotwig',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.PTF:HiroTopology',
        label='HiroTopology',
        description='Describes a Hiro topology for performance tests.',
        valid='start=2019-01-22;',
        created_by='TGotwig',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.PTF:Test',
        label='Test',
        description='Describes most important input and output entities of each test outcome.',
        valid='start=2019-01-22;',
        created_by='TGotwig',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Parameter',
        label='Parameter',
        description='Defines a parameter of an entity, for example: service, action, ticket, sla, etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:ParameterType',
        label='ParameterType',
        description='Allows to define more details about the values of a Parameter the Parameter will be linked to a ParameterType \nby the \"uses\" relationship. Each Parameter can have only one those connection.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Penalty',
        label='Penalty',
        description='Defines the penalty that has to be paid in certain circumstances',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Person',
        label='Person',
        description='A Person represents a human identity.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Policy',
        label='Policy',
        description='A policy is a deliberate system of principles to guide decisions and achieve rational outcomes. It is connected and applied to Organizations',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Price:Invoice',
        label='Invoice',
        description='Models any type of invoice',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Price:PriceSpecification',
        label='PriceSpecification',
        description='Models a price specification for any type of IT service, component or task',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Procurement:ProductionOrder',
        label='ProductionOrder',
        description='A production order in the procurement process.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Procurement:PurchaseOrder',
        label='PurchaseOrder',
        description='A purchase order in the procurement process.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Procurement:PurchaseOrderItem',
        label='PurchaseOrderItem',
        description='An individual item within a purchase order in the procurement process.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Product',
        label='Product',
        description='A commercially distributed good or service',
        valid='start=2018-02-08;',
        created_by='Viktor Voss',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Project:Milestone',
        label='Milestone',
        description='An identity that represents an important event, achievement, ...',
        valid='start=2016-08-08;',
        created_by='Arthur Shoba',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Project:Project',
        label='Project',
        description='An identity that represents a grouping of Person, Milestone objects.',
        valid='start=2016-08-08;',
        created_by='Arthur Shoba',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Question',
        label='Question',
        description='This structure allows an automation engine to create data requests for existing Issues which should be filled by human user. \nAdditionaly could be used to create new Issue from some form.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.RDDL:Namespace',
        label='Namespace',
        description='An XML namespace.',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RDDL:Resource',
        label='Resource',
        description='RDF Schema for RDDL: 2001-01-29',
        valid='start=2016-09-22;',
        created_by='OGIT Importer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:Controller',
        label='Controller',
        description='Controller to control the robot.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:Object',
        label='Object',
        description='An object is anything that has a fixed shape or form, that you can touch or see, and that is not alive.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:Robot',
        label='Robot',
        description='A robot is a machine—especially one programmable by a computer— capable of carrying out a complex series of actions automatically.\n\t                        Robots can be guided by an external control device or the control may be embedded within.\n\t                        Robots are machines designed to perform a task with no regard to how they look.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:RoboticEnvironment',
        label='RoboticEnvironment',
        description='An known environment to Robot where its operates.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:RoboticSystem',
        label='RoboticSystem',
        description='An integrated system which used robots for automation.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.RPA:Sensor',
        label='Sensor',
        description='Sensor is a device, module, or subsystem whose purpose is to detect events or changes in its environment and send the information to other electronics, frequently a computer processor.\n\t                    example sensors are Lasser Scanner, Camera etc.',
        valid='start=2019-03-21;',
        created_by='Kaushik Gondaliya',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Rating',
        label='Rating',
        description='Rating is used to rank nodes based on an arbitrary integer `value`',
        valid='start=2018-08-01;',
        created_by='qikram@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Region',
        label='Region',
        description='A region is always something that has a certain geographic extension (a country, a county,  ) whereas ogit/Location usually refers to specific place usually having an address',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Relevance',
        label='Relevance',
        description='define importance of connection between two entities',
        valid='start=2019-07-23;',
        created_by='Kaushik Gondaliya ',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Role',
        label='Role',
        description='In contrast to ogit/Organization, which is mainly a collection of persons and/or other organziations, ogit/Role defines behavior of an actor along with necessary privileges.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.SaaS:Component',
        label='Component',
        description='Entities of this kind form the catalogue of components a SaaS Deployment can consist of',
        valid='start=2020-01-14;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SaaS:ComponentInstance',
        label='ComponentInstance',
        description='An instance of a Component within a Deployment',
        valid='start=2020-01-14;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SaaS:ConfigurationTemplate',
        label='ConfigurationTemplate',
        description='Specifies a certain installation flavor of a Component. Might fix same configuration parameters and provide defaults for some others. Will be used within DeploymentTemplate to form a deployable template of several components',
        valid='start=2020-01-14;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SaaS:Deployment',
        label='Deployment',
        description='represents a Deployment in any possible state. Will be instantiated from a DeploymentTemplate',
        valid='start=2020-01-14;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SaaS:DeploymentTemplate',
        label='DeploymentTemplate',
        description='Specifies templates that can be instantiated as a Deployment. When instantiated all contained ConfigurationTemplates will be instantiated as ComponentConfigs',
        valid='start=2020-01-14;',
        created_by='FCO',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Customer',
        label='Customer',
        description='A customer in the sales and distribution process.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Delivery',
        label='Delivery',
        description='A delivery in the sales and distribution process.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:DeliveryItem',
        label='DeliveryItem',
        description='An individual item contained in a delivery in the sales and distribution process.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Equipment',
        label='Equipment',
        description='Equipment used in the sales order process, e.g. a vehicle.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Invoice',
        label='Invoice',
        description='An invoice for a sales order.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:InvoiceItem',
        label='InvoiceItem',
        description='An individual item on a sales order invoice.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:OpenItem',
        label='OpenItem',
        description='An open item in the sales and distribution process.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Payment',
        label='Payment',
        description='A payment in the sales and distribution process.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:SalesOrder',
        label='SalesOrder',
        description='A sales order placed by a customer.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:SalesOrderItem',
        label='SalesOrderItem',
        description='An individual item on a sales order.',
        valid='start=2019-07-10;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:Shipment',
        label='Shipment',
        description='A shipment in the sales and distribution process.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.SalesDistribution:ShipmentItem',
        label='ShipmentItem',
        description='An individual item contained in a shipment in the sales and distribution process.',
        valid='start=2020-12-15;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Schedule:Activity',
        label='Activity',
        description='An activity planned as part of a schedule.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Schedule:Attendee',
        label='Attendee',
        description='An attendee of a calendar event.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Schedule:Calendar',
        label='Calendar',
        description='A calendar containing events.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Schedule:Event',
        label='Event',
        description='An event planned or occuring as part of a calendar.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Schedule:Schedule',
        label='Schedule',
        description='A schedule consisting of planned activities.',
        valid='start=2019-07-02;',
        created_by='Marek Meyer',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Schema',
        label='Schema',
        description='Any type of schema, could be defined in XSD, YAML, etc.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Series',
        label='Series',
        description='Any kind of series',
        valid='start=2017-04-19;',
        created_by='stravlos@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.ServiceManagement:Action',
        label='Action',
        description='Defines Actions on it Services. A Service is connected to the available Actions by the \"supports\" relationship.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:ApprovalTask',
        label='ApprovalTask',
        description='This entity type defines approval tasks for a ticket. Used for example at ogit/ServiceManagement/ChangeRequest.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:ChangeRequest',
        label='ChangeRequest',
        description='This entity type defines a change request ticket',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Incident',
        label='Incident',
        description='This entity type defines an incident ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Offering',
        label='Offering',
        description='This is a concrete offering from a vendor including one or more combined services from a catalog/collection/offering book.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Order',
        label='Order',
        description='Defines an order.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Problem',
        label='Problem',
        description='This entity type defines a problem ticket.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Report',
        label='Report',
        description='Reporting about IT service delivery',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:SLA',
        label='SLA',
        description='A service level agreement.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Service',
        label='Service',
        description='A technology service item, which combined or not with other technology services can constitute a service offering (ogit/ServiceManagement/Offering).',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:SubTask',
        label='SubTask',
        description='This entity type defines sub-tasks for a ticket. Mostly used for ChangeRequest.\nComman alternative names with same meaning are: task, activity, work order.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.ServiceManagement:Ticket',
        label='Ticket',
        description='This entity defines any type of tickets. For specific behaviour of tickets, please check specific entities (e.g. ogit/ServiceManagement/Incident).',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Software:Application',
        label='Application',
        description='Represents any type of software application',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Software:Connector',
        label='Connector',
        description='Represents any type of software connector',
        valid='start=2015-06-11;',
        created_by='Aymen Ayoub',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Software:Data',
        label='Data',
        description='Data transmitted between two components via connection.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Software:SoftwareComponent',
        label='SoftwareComponent',
        description='Any type of Software Component',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Software:SoftwareConnection',
        label='SoftwareConnection',
        description='Represents the connection between two components, which allows data transmission through a network link.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Statistics:AutomationFamily',
        label='AutomationFamily',
        description='AutomationFamily defines the group of cases for automation of IT environment and its functionality.',
        valid='start=2016-03-07;',
        created_by='Liudmyla Nechepurenko',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Status',
        label='Status',
        description='Any kind of status',
        valid='start=2017-04-19;',
        created_by='stravlos@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Subscription',
        label='Subscription',
        description='A Subscription to an Event.',
        valid='start=2018-03-22;',
        created_by='qikram@arago.de',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.Survey:Iteration',
        label='Iteration',
        description='Iteration of the same survey',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Survey:Reply',
        label='Reply',
        description='User\'s reply on a survey',
        valid='start=2016-08-08;',
        created_by='Alexander Ryabtsev',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.Survey:Survey',
        label='Survey',
        description='List with questions',
        valid='start=2016-07-12;',
        created_by='Arthur Shoba',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Tag',
        label='Tag',
        description='An Tag is a customer defined tag to help filter data',
        valid='start=2020-08-04;',
        created_by='Ben Neal',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Task',
        label='Task',
        description='A task is a unit of execution.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:TaskList',
        label='TaskList',
        description='A task list consists of one or many tasks.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:TermsAndConditions',
        label='TermsAndConditions',
        description='Terms and conditions contains terms of use to be accepted by users',
        valid='start=2018-04-18;',
        created_by='Aman Kubanychbek',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:Timeseries',
        label='Timeseries',
        description='A time series is a sequence of data points, measured typically at successive points in time spaced at uniform time intervals.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit.UserMeta:Filter',
        label='Filter',
        description='A filter set by user, indicating preferences',
        valid='start=2016-07-19;',
        created_by='stravlos@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.UserMeta:Game',
        label='Game',
        description='Something which is played to obtain meta data around user behaviour and perception',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.UserMeta:Preferences',
        label='Preferences',
        description='User Preferences is a part of the User Model, a collection of information that describes the user’s needs, preferences and interests',
        valid='start=2018-10-01;',
        created_by='amerdeev@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit.UserMeta:Question',
        label='Question',
        description='A question which is part of a game, played to obtain meta data around user behaviour and perception',
        valid='start=2016-07-19;',
        created_by='bneal@arago.de',
        scope=Scope.NTO)
    yield Entity(
        about='ogit:Vcard',
        label='Vcard',
        description='vCard is a specification developed by the IETF for the description of people and organisations. Recently, vCard has been \nsignificantly updated to Version 4 as documented in [RFC6350]. Typically, vCard objects are encoded in its own defined \ntext-based syntax or XML renderings.',
        valid='start=2015-05-21;',
        created_by='Peter Larem',
        scope=Scope.SGO)
    yield Entity(
        about='ogit:VersioningData',
        label='VersioningData',
        description='Proxy node for accessing any versioned data.',
        valid='start=2017-10-31;',
        hide=True,
        created_by='druss@arago.de',
        scope=Scope.SGO)
    # </editor-fold>


# noinspection SpellCheckingInspection
def entity_refs() -> Generator[Entity, None, None]:
    # <editor-fold desc="generated entity refs">
    yield Entity(
        about='ogit:Account',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:email',
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:connects', 'ogit:Person'),
            ('ogit:follows', 'ogit:Account')})
    yield Entity(
        about='ogit.Accounting:CategoryItem',
        parent='ogit:Node',
        required_attributes={'ogit.Accounting:subtype'},
        optional_attributes={
            'ogit.Accounting:balance',
            'ogit.Accounting:rank',
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit.Accounting:contributesTo', 'ogit.Accounting:FinancialStatement'),
            ('ogit.Accounting:includes', 'ogit.Accounting:CategoryItem')})
    yield Entity(
        about='ogit.Accounting:CompanyEntity',
        parent='ogit:Node',
        optional_attributes={'ogit.Accounting:accountingStandard'},
        allowed_connections={
            ('ogit.Accounting:has', 'ogit.Accounting:ConfigItem'),
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:contains', 'ogit.Accounting:CompanySpecificCategorization'),
            ('ogit:corresponds', 'ogit.Accounting:CompanyEntity'),
            ('ogit:generates', 'ogit.Accounting:FinancialStatement'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:has', 'ogit:Relevance')})
    yield Entity(
        about='ogit.Accounting:CompanySpecificCategorization',
        parent='ogit:Node',
        allowed_connections={('ogit:contains', 'ogit.Accounting:CompanyEntity')})
    yield Entity(
        about='ogit.Accounting:ConfigItem',
        parent='ogit:Node',
        required_attributes={'ogit.Accounting:subtype'},
        optional_attributes={
            'ogit.Accounting:NAOCategorizations',
            'ogit.Accounting:TrialBalanceTargetAccountByNumber',
            'ogit.Accounting:detailedCategories',
            'ogit.Accounting:mainCategories'})
    yield Entity(
        about='ogit.Accounting:DDTarget',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:generates', 'ogit.Accounting:FinancialStatement')})
    yield Entity(
        about='ogit.Accounting:FinancialStatement',
        parent='ogit:Node',
        required_attributes={'ogit.Accounting:subtype'},
        optional_attributes={
            'ogit.Accounting:periods',
            'ogit.Accounting:primaryReportingPeriod',
            'ogit.Accounting:template',
            'ogit:currency',
            'ogit:language'},
        allowed_connections={
            ('ogit:contains', 'ogit.Accounting:CategoryItem'),
            ('ogit:contains', 'ogit.Accounting:LineItem')})
    yield Entity(
        about='ogit.Accounting:LineItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Accounting:AccountNumber',
            'ogit.Accounting:association',
            'ogit.Accounting:balance',
            'ogit.Accounting:subtype',
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit.Accounting:contributesTo', 'ogit.Accounting:FinancialStatement'),
            ('ogit.Accounting:maps', 'ogit.Accounting:CategoryItem'),
            ('ogit:contains', 'ogit.Accounting:LineItem'),
            ('ogit:generates', 'ogit.Accounting:LineItem')})
    yield Entity(
        about='ogit.Advertising:Advertiser',
        parent='ogit:Node',
        optional_attributes={
            'ogit:category',
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:contains', 'ogit.Advertising:Campaign'),
            ('ogit:contains', 'ogit.Advertising:InsertionOrder')})
    yield Entity(
        about='ogit.Advertising:Campaign',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:consistsOf', 'ogit.Advertising:Creative'),
            ('ogit:consistsOf', 'ogit.Advertising:InsertionOrder'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Advertising:CampaignManager',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:manages', 'ogit.Advertising:Campaign'),
            ('ogit:manages', 'ogit.Advertising:MediaPlan'),
            ('ogit:supervises', 'ogit.Advertising:Platform')})
    yield Entity(
        about='ogit.Advertising:Client',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:owns', 'ogit.Advertising:Campaign'),
            ('ogit:owns', 'ogit.Advertising:MediaPlan')})
    yield Entity(
        about='ogit.Advertising:Creative',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'})
    yield Entity(
        about='ogit.Advertising:InsertionOrder',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:consistsOf', 'ogit.Advertising:LineItem'),
            ('ogit:generates', 'ogit.Documents:Spreadsheet'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:uses', 'ogit.Advertising:Creative')})
    yield Entity(
        about='ogit.Advertising:LineItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:generates', 'ogit.Documents:Spreadsheet'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:uses', 'ogit.Advertising:Creative')})
    yield Entity(
        about='ogit.Advertising:MediaPlan',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={('ogit:includes', 'ogit.Advertising:Campaign')})
    yield Entity(
        about='ogit.Advertising:Platform',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:type'},
        allowed_connections={
            ('ogit:contains', 'ogit.Advertising:Advertiser'),
            ('ogit:hosts', 'ogit.Advertising:Campaign'),
            ('ogit:hosts', 'ogit.Advertising:InsertionOrder')})
    yield Entity(
        about='ogit:Alert',
        parent='ogit:Node',
        required_attributes={
            'ogit:category',
            'ogit:creator',
            'ogit:type'},
        optional_attributes={
            'ogit:function',
            'ogit:value'},
        allowed_connections={
            ('ogit:alerts', 'ogit:Person'),
            ('ogit:contains', 'ogit:Contract'),
            ('ogit:contains', 'ogit:License'),
            ('ogit:triggers', 'ogit:Event')})
    yield Entity(
        about='ogit:Asset',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:associates', 'ogit.Cost:CostElement'),
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:contains', 'ogit:Contract'),
            ('ogit:describes', 'ogit.Automation:MARSNode'),
            ('ogit:describes', 'ogit.Automation:MARSNodeTemplate'),
            ('ogit:describes', 'ogit.Datacenter:Cooling'),
            ('ogit:describes', 'ogit.Datacenter:PowerDistributionUnit'),
            ('ogit:describes', 'ogit.Datacenter:Rack'),
            ('ogit:describes', 'ogit:Device'),
            ('ogit:describes', 'ogit.MARS:Machine'),
            ('ogit:describes', 'ogit.MARS:Software'),
            ('ogit:describes', 'ogit.Network:NetworkCard'),
            ('ogit:describes', 'ogit.Network:NetworkEnclosure'),
            ('ogit:describes', 'ogit.Network:NetworkFabric'),
            ('ogit:describes', 'ogit.Network:SimpleDevice'),
            ('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit:Attachment',
        parent='ogit:Node',
        optional_attributes={
            'ogit:accessControl',
            'ogit:content',
            'ogit:createdAt',
            'ogit:creator',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:lastUpdatedBy',
            'ogit:name',
            'ogit:size',
            'ogit:sourceTable',
            'ogit:type',
            'ogit:url'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Auth:AccountProfile'),
            ('ogit:belongs', 'ogit.Automation:MARSNode'),
            ('ogit:belongs', 'ogit:Comment'),
            ('ogit:belongs', 'ogit:Contract'),
            ('ogit:belongs', 'ogit.Factory:Plant'),
            ('ogit:belongs', 'ogit:License'),
            ('ogit:belongs', 'ogit.MARS:Application'),
            ('ogit:belongs', 'ogit.MARS:Machine'),
            ('ogit:belongs', 'ogit.MARS:Resource'),
            ('ogit:belongs', 'ogit.MARS:Software'),
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:belongs', 'ogit:Person'),
            ('ogit:belongs', 'ogit.SaaS:ComponentInstance'),
            ('ogit:belongs', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:belongs', 'ogit.ServiceManagement:Incident'),
            ('ogit:belongs', 'ogit.ServiceManagement:Order'),
            ('ogit:belongs', 'ogit.ServiceManagement:Problem'),
            ('ogit:belongs', 'ogit.ServiceManagement:SubTask'),
            ('ogit:belongs', 'ogit.ServiceManagement:Ticket')})
    yield Entity(
        about='ogit.Audit:Audit',
        parent='ogit:Node',
        optional_attributes={
            'ogit:name',
            'ogit:title'},
        allowed_connections={
            ('ogit:affects', 'ogit.FinancialAccounting:Company'),
            ('ogit:contains', 'ogit.Audit:Batch')})
    yield Entity(
        about='ogit.Audit:Batch',
        parent='ogit:Node',
        optional_attributes={
            'ogit:name',
            'ogit:title'},
        allowed_connections={
            ('ogit:contains', 'ogit.Audit:Sample'),
            ('ogit:has', 'ogit:Attachment')})
    yield Entity(
        about='ogit.Audit:Sample',
        parent='ogit:Node',
        optional_attributes={
            'ogit:creationTime',
            'ogit:name',
            'ogit:title'},
        allowed_connections={('ogit:contains', 'ogit.Documents:Document')})
    yield Entity(
        about='ogit.Auth:Account',
        parent='ogit:Node',
        required_attributes={
            'ogit.Auth.Account:type',
            'ogit:name',
            'ogit:status'},
        optional_attributes={
            'ogit.Auth.Account:acceptedPrivacy',
            'ogit.Auth.Account:acceptedProjectTerms',
            'ogit.Auth.Account:acceptedTerms',
            'ogit.Auth.Account:allowCookies',
            'ogit.Auth.Account:statusReason',
            'ogit:email'},
        allowed_connections={
            ('ogit.Auth:assumes', 'ogit.Auth:Role'),
            ('ogit.Auth:consents', 'ogit.Auth:Application'),
            ('ogit.Auth:isMemberOf', 'ogit.Auth:Organization'),
            ('ogit.Auth:isMemberOf', 'ogit.Auth:Team'),
            ('ogit.Auth:uses', 'ogit.Auth:Application'),
            ('ogit.Auth:uses', 'ogit.SaaS:ComponentInstance'),
            ('ogit:accepts', 'ogit:TermsAndConditions'),
            ('ogit:belongs', 'ogit:Person'),
            ('ogit:consumes', 'ogit.Project:Milestone'),
            ('ogit:consumes', 'ogit.Project:Project'),
            ('ogit:creates', 'ogit.Auth:ApplicationReview'),
            ('ogit:defines', 'ogit.UserMeta:Filter'),
            ('ogit:manages', 'ogit:Subscription'),
            ('ogit:produces', 'ogit.Project:Milestone'),
            ('ogit:produces', 'ogit.Project:Project'),
            ('ogit:provides', 'ogit:Rating'),
            ('ogit:repliedWith', 'ogit.Survey:Reply'),
            ('ogit:supervises', 'ogit:Contract'),
            ('ogit:supervises', 'ogit.Project:Project'),
            ('ogit:supports', 'ogit.Project:Milestone'),
            ('ogit:supports', 'ogit.Project:Project')})
    yield Entity(
        about='ogit.Auth:AccountProfile',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Auth.Account:acceptedEmails',
            'ogit.Auth.Account:defaultScope',
            'ogit.Auth.Account:defaultTeam',
            'ogit.Auth.Account:displayName',
            'ogit:firstName',
            'ogit:lastName'},
        allowed_connections={('ogit.Auth:belongs', 'ogit.Auth:Account')})
    yield Entity(
        about='ogit.Auth:Application',
        parent='ogit:Node',
        required_attributes={
            'ogit.Auth:edgeRule',
            'ogit.Auth:vertexRule',
            'ogit:description',
            'ogit:name'},
        optional_attributes={
            'ogit.Auth.Application:parent',
            'ogit.Auth.Application:status',
            'ogit.Auth.Application:type',
            'ogit.Auth.Application:urls',
            'ogit.Auth:allowedTypes'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:includes', 'ogit:Notification'),
            ('ogit:versions', 'ogit.Auth:Application')})
    yield Entity(
        about='ogit.Auth:ApplicationReview',
        parent='ogit:Node',
        required_attributes={
            'ogit:status',
            'ogit:title'},
        optional_attributes={'ogit:comment'},
        allowed_connections={('ogit:reviews', 'ogit.Auth:Application')})
    yield Entity(
        about='ogit.Auth:Configuration',
        parent='ogit:Node',
        allowed_connections={('ogit.Auth:belongs', 'ogit.Auth:Organization')})
    yield Entity(
        about='ogit.Auth:DataScope',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={('ogit.Auth:belongs', 'ogit.Auth:Organization')})
    yield Entity(
        about='ogit.Auth:DataSet',
        parent='ogit:Node',
        required_attributes={
            'ogit.Auth:edgeRule',
            'ogit.Auth:vertexRule',
            'ogit:name'},
        optional_attributes={
            'ogit.Auth:restricted',
            'ogit:description'})
    yield Entity(
        about='ogit.Auth:OrgDomain',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={('ogit.Auth:belongs', 'ogit.Auth:Organization')})
    yield Entity(
        about='ogit.Auth:Organization',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:isInternal',
            'ogit:status'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:concludes', 'ogit:Contract'),
            ('ogit:consumes', 'ogit.Project:Project'),
            ('ogit:consumes', 'ogit.Survey:Iteration'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:produces', 'ogit.Project:Project'),
            ('ogit:produces', 'ogit.Survey:Iteration'),
            ('ogit:supports', 'ogit.Project:Project'),
            ('ogit:supports', 'ogit.Survey:Iteration')})
    yield Entity(
        about='ogit.Auth:Role',
        parent='ogit:Node',
        required_attributes={
            'ogit.Auth:edgeRule',
            'ogit.Auth:vertexRule',
            'ogit:name'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.Auth:RoleAssignment',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.Auth:assigns', 'ogit.Auth:DataSet'),
            ('ogit.Auth:assigns', 'ogit.Auth:Role'),
            ('ogit.Auth:assigns', 'ogit.Auth:Team'),
            ('ogit.Auth:belongs', 'ogit.Auth:Organization')})
    yield Entity(
        about='ogit.Auth:Team',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={
            ('ogit.Auth:belongs', 'ogit.Auth:Organization'),
            ('ogit.Auth:belongs', 'ogit.Auth:Team'),
            ('ogit:approves', 'ogit.Automation:KnowledgeItem'),
            ('ogit:approves', 'ogit.Knowledge:AcquisitionSession'),
            ('ogit:rejects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:rejects', 'ogit.Knowledge:AcquisitionSession')})
    yield Entity(
        about='ogit.Automation:ActionApplicability',
        parent='ogit:Node',
        required_attributes={'ogit.Automation:environmentFilter'},
        optional_attributes={
            'ogit.Automation:mandatoryParameters',
            'ogit.Automation:optionalParameters'},
        allowed_connections={('ogit:provides', 'ogit.Automation:ActionCapability')})
    yield Entity(
        about='ogit.Automation:ActionCapability',
        parent='ogit:Node',
        required_attributes={
            'ogit.Automation:mandatoryParameters',
            'ogit:description',
            'ogit:name'},
        optional_attributes={'ogit.Automation:optionalParameters'})
    yield Entity(
        about='ogit.Automation:ActionHandler',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit.Automation:optionalParameters'},
        allowed_connections={('ogit:provides', 'ogit.Automation:ActionApplicability')})
    yield Entity(
        about='ogit.Automation:AutomationIssue',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Automation:deployStatus',
            'ogit.Automation:isDeployed',
            'ogit.Automation:issueFormalRepresentation',
            'ogit.Automation:issueType',
            'ogit.Automation:maxIdleTime',
            'ogit.Automation:originNode',
            'ogit.Automation:parentIssue',
            'ogit.Automation:processingNode',
            'ogit.Automation:processingTimestamp',
            'ogit.Automation:suspendUntil',
            'ogit.Automation:webhook',
            'ogit.RL:state',
            'ogit.RL:totalReward',
            'ogit:creationTime',
            'ogit:modificationTime',
            'ogit:status',
            'ogit:subject'},
        indexed_attributes={
            'ogit.Automation:issueFormalRepresentation',
            'ogit:subject'},
        allowed_connections={
            ('ogit:associates', 'ogit:Question'),
            ('ogit:contains', 'ogit.Automation:DynamicEngineData'),
            ('ogit:contains', 'ogit.Automation:Item'),
            ('ogit:contains', 'ogit:Task'),
            ('ogit:generates', 'ogit.Automation:History'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.Knowledge:AcquisitionSession'),
            ('ogit:worksOn', 'ogit.Automation:MARSNode')})
    yield Entity(
        about='ogit.Automation:Configuration',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:uses', 'ogit.Automation:ActionHandler'),
            ('ogit:uses', 'ogit.Automation:KIRanking'),
            ('ogit:uses', 'ogit.Automation:KnowledgePool')})
    yield Entity(
        about='ogit.Automation:DynamicEngineData',
        parent='ogit:Node',
        optional_attributes={
            'ogit:creationTime',
            'ogit:modificationTime',
            'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit.Automation:DynamicEngineData')})
    yield Entity(
        about='ogit.Automation:History',
        parent='ogit:Node',
        required_attributes={
            'ogit.Automation:affectedNodeId',
            'ogit.Automation:command',
            'ogit.Automation:knowledgeItemId',
            'ogit.Automation:logLevel',
            'ogit:message',
            'ogit:timestamp'},
        allowed_connections={('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Automation:Item',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Automation:Item'),
            ('ogit:contains', 'ogit.Automation:KnowledgeItemAttribute')})
    yield Entity(
        about='ogit.Automation:KIRanking',
        parent='ogit:Node',
        required_attributes={
            'ogit.Automation:rankingType',
            'ogit.Automation:weightMap',
            'ogit:name'},
        optional_attributes={
            'ogit.Automation:defaultRank',
            'ogit.Automation:defaultSigma',
            'ogit.Automation:rankMap',
            'ogit.Automation:sendData',
            'ogit.Automation:sendHistory',
            'ogit:url'})
    yield Entity(
        about='ogit.Automation:KnowledgeBundle',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:accessControl'},
        allowed_connections={
            ('ogit:contains', 'ogit.Automation:KnowledgeItem'),
            ('ogit:derivesFrom', 'ogit.Automation:KnowledgeBundle')})
    yield Entity(
        about='ogit.Automation:KnowledgeItem',
        parent='ogit:Node',
        required_attributes={'ogit.Automation:knowledgeItemFormalRepresentation'},
        optional_attributes={
            'ogit.Automation:deployStatus',
            'ogit.Automation:deployToEngine',
            'ogit.Automation:isDeployed',
            'ogit.Automation:knowledgeItemSyntaxVersion',
            'ogit.Automation:knowledgeItemTier',
            'ogit:_tags',
            'ogit:accessControl',
            'ogit:changeLog',
            'ogit:creationTime',
            'ogit:description',
            'ogit:isValid',
            'ogit:modificationTime',
            'ogit:name'},
        indexed_attributes={
            'ogit:_tags',
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit.Forum:WorkflowStep'),
            ('ogit:connects', 'ogit:Hyperlink'),
            ('ogit:contains', 'ogit.Automation:Trigger'),
            ('ogit:deployedTo', 'ogit.OSLC-crtv:ServiceInstance'),
            ('ogit:derivesFrom', 'ogit.Automation:KnowledgeItem'),
            ('ogit:forks', 'ogit.Automation:KnowledgeItem'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:relates', 'ogit.Automation:MARSNodeTemplate'),
            ('ogit:solves', 'ogit:Task'),
            ('ogit:worksOn', 'ogit.Automation:AutomationIssue')})
    yield Entity(
        about='ogit.Automation:KnowledgeItemAttribute',
        parent='ogit:Node',
        required_attributes={
            'ogit:name',
            'ogit:value'},
        optional_attributes={'ogit:mode'})
    yield Entity(
        about='ogit.Automation:KnowledgePool',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Automation:KnowledgeBundle'),
            ('ogit:contains', 'ogit.Automation:KnowledgeItem'),
            ('ogit:uses', 'ogit.Automation:KnowledgeItem')})
    yield Entity(
        about='ogit.Automation:MAID',
        parent='ogit:Node',
        required_attributes={'ogit.Automation:maidFormalRepresentation'},
        allowed_connections={
            ('ogit:defines', 'ogit:Timeseries'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Automation:MARSModel',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Automation:MARSNode'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:implements', 'ogit.ServiceManagement:Order')})
    yield Entity(
        about='ogit.Automation:MARSModelTemplate',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={('ogit:contains', 'ogit.Automation:MARSNodeTemplate')})
    yield Entity(
        about='ogit.Automation:MARSNode',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Automation:additionalMacAddress',
            'ogit.Automation:adminUrl',
            'ogit.Automation:appInfrastructureType',
            'ogit.Automation:appInstanceType',
            'ogit.Automation:appServer',
            'ogit.Automation:basicConfigId',
            'ogit.Automation:brand',
            'ogit.Automation:buildName',
            'ogit.Automation:buildType',
            'ogit.Automation:companyName',
            'ogit.Automation:contextPath',
            'ogit.Automation:cpuCoreCount',
            'ogit.Automation:cpuCount',
            'ogit.Automation:cpuManufacturer',
            'ogit.Automation:cpuModel',
            'ogit.Automation:cpuSpeed',
            'ogit.Automation:cpuType',
            'ogit.Automation:dataClassification',
            'ogit.Automation:dataPrivacy',
            'ogit.Automation:databaseSchema',
            'ogit.Automation:databaseServer',
            'ogit.Automation:deployStatus',
            'ogit.Automation:diskCount',
            'ogit.Automation:diskSpace',
            'ogit.Automation:domain',
            'ogit.Automation:exchangeRate',
            'ogit.Automation:firewallStatus',
            'ogit.Automation:firmwareVersion',
            'ogit.Automation:fqdn',
            'ogit.Automation:host',
            'ogit.Automation:installCount',
            'ogit.Automation:installPath',
            'ogit.Automation:isDeployed',
            'ogit.Automation:licenseAvailability',
            'ogit.Automation:licenseName',
            'ogit.Automation:licenseType',
            'ogit.Automation:lifecycle',
            'ogit.Automation:marsNodeFormalRepresentation',
            'ogit.Automation:marsNodeType',
            'ogit.Automation:memory',
            'ogit.Automation:middlewareType',
            'ogit.Automation:moveToProductionAt',
            'ogit.Automation:objectIdentifier',
            'ogit.Automation:osKey',
            'ogit.Automation:osLicense',
            'ogit.Automation:osManufacturer',
            'ogit.Automation:osName',
            'ogit.Automation:osServicePack',
            'ogit.Automation:osVersion',
            'ogit.Automation:patchNumber',
            'ogit.Automation:portNumber',
            'ogit.Automation:portNumberListener',
            'ogit.Automation:projectName',
            'ogit.Automation:serialNumber',
            'ogit.Automation:serviceId',
            'ogit.Automation:serviceName',
            'ogit.Automation:serviceStatus',
            'ogit.Automation:serviceType',
            'ogit.Automation:servletClass',
            'ogit.Automation:servletName',
            'ogit.Automation:software',
            'ogit.Automation:softwareKey',
            'ogit.Automation:systemClass',
            'ogit.Automation:systemType',
            'ogit.Automation:tcpPort',
            'ogit.Automation:virtualMachineName',
            'ogit.Automation:virtualSystemName',
            'ogit.Automation:virtualSystemType',
            'ogit.Automation:webServer',
            'ogit.Datacenter:rackUnit',
            'ogit:connectorId',
            'ogit:creationTime',
            'ogit:endOfWarranty',
            'ogit:id',
            'ogit:ipAddress',
            'ogit:macAddress',
            'ogit:manufacturer',
            'ogit:modificationTime',
            'ogit:name',
            'ogit:serialNumber'},
        indexed_attributes={
            'ogit.Automation:marsNodeFormalRepresentation',
            'ogit:name'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit.ServiceManagement:Service'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:associates', 'ogit.Cost:CostElement'),
            ('ogit:contains', 'ogit.Automation:DynamicEngineData'),
            ('ogit:contains', 'ogit.Automation:MARSNode'),
            ('ogit:contains', 'ogit.Network:NetworkInterface'),
            ('ogit:corresponds', 'ogit.Software:Application'),
            ('ogit:dependsOn', 'ogit.Automation:MARSNode'),
            ('ogit:deployedTo', 'ogit.Automation:MARSNode'),
            ('ogit:generates', 'ogit.Data:Log'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:hosts', 'ogit.Automation:MARSNode'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:locatedIn', 'ogit:Region'),
            ('ogit:provides', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.Automation:KnowledgeItem'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.Automation:MARSNodeTemplate'),
            ('ogit:relates', 'ogit:License'),
            ('ogit:runsOn', 'ogit.Automation:MARSNode'),
            ('ogit:uses', 'ogit.Automation:Configuration')})
    yield Entity(
        about='ogit.Automation:MARSNodeTemplate',
        parent='ogit:Node',
        required_attributes={'ogit.Automation:marsNodeFormalRepresentation'},
        optional_attributes={
            'ogit.Automation:marsNodeType',
            'ogit:status'},
        allowed_connections={
            ('ogit:associates', 'ogit.Cost:CostElement'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.Automation:MARSNodeTemplate'),
            ('ogit:relates', 'ogit.Automation:MARSNodeTemplate')})
    yield Entity(
        about='ogit.Automation:Trigger',
        parent='ogit:Node',
        required_attributes={'ogit:description'},
        allowed_connections={('ogit:contains', 'ogit.Automation:Item')})
    yield Entity(
        about='ogit.Automation:Variable',
        parent='ogit:Node',
        required_attributes={
            'ogit.Automation:todo',
            'ogit:_id',
            'ogit:accessControl',
            'ogit:creator',
            'ogit:description',
            'ogit:name'},
        optional_attributes={'ogit:_tags'})
    yield Entity(
        about='ogit:Catalog',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:id',
            'ogit:type',
            'ogit:version'},
        allowed_connections={
            ('ogit:contains', 'ogit:Catalog'),
            ('ogit:contains', 'ogit:CatalogItem'),
            ('ogit:contains', 'ogit.Factory:Plant'),
            ('ogit:contains', 'ogit.MRP:NormItem'),
            ('ogit:contains', 'ogit.MRP:Part'),
            ('ogit:validFor', 'ogit:Region')})
    yield Entity(
        about='ogit:CatalogItem',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={
            ('ogit:requires', 'ogit:CatalogItem'),
            ('ogit:requires', 'ogit.ServiceManagement:Action'),
            ('ogit:requires', 'ogit.ServiceManagement:Service')})
    yield Entity(
        about='ogit:Certificate',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:subject',
            'ogit:validFrom',
            'ogit:validTo'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:relates', 'ogit:Installation')})
    yield Entity(
        about='ogit:Comment',
        parent='ogit:Node',
        optional_attributes={
            'ogit:content',
            'ogit:creator',
            'ogit:id'},
        allowed_connections={
            ('ogit.Forum:mentions', 'ogit.Forum:Profile'),
            ('ogit:belongs', 'ogit:Event'),
            ('ogit:belongs', 'ogit.ServiceManagement:SubTask'),
            ('ogit:belongs', 'ogit.ServiceManagement:Ticket'),
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit:Contract'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit:Hyperlink'),
            ('ogit:connects', 'ogit:License'),
            ('ogit:connects', 'ogit:Organization'),
            ('ogit:connects', 'ogit:Person'),
            ('ogit:responds', 'ogit.Forum:Rating'),
            ('ogit:responds', 'ogit.Forum:Reply'),
            ('ogit:seenBy', 'ogit.Auth:Account')})
    yield Entity(
        about='ogit:Configuration',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit:ConfigurationItem',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.Automation:governingContract',
            'ogit:asset',
            'ogit:assetTag',
            'ogit:assignedAt',
            'ogit:availability',
            'ogit:businessCriticality',
            'ogit:category',
            'ogit:checkedInAt',
            'ogit:checkedOutAt',
            'ogit:ciType',
            'ogit:class',
            'ogit:comment',
            'ogit:confidentiality',
            'ogit:contact',
            'ogit:content',
            'ogit:createdAt',
            'ogit:deliveredAt',
            'ogit:description',
            'ogit:endOfWarranty',
            'ogit:externalId',
            'ogit:faultCount',
            'ogit:impact',
            'ogit:installStatus',
            'ogit:installedAt',
            'ogit:integrity',
            'ogit:inventoryNumber',
            'ogit:invoiceNumber',
            'ogit:isCritical',
            'ogit:isSupported',
            'ogit:lastScannedAt',
            'ogit:lastUpdatedAt',
            'ogit:leaseContract',
            'ogit:model',
            'ogit:modelNumber',
            'ogit:name',
            'ogit:operationalStatus',
            'ogit:orderedAt',
            'ogit:pendingChange',
            'ogit:priority',
            'ogit:productOrderNumber',
            'ogit:purchasedAt',
            'ogit:securityClass',
            'ogit:serviceContract',
            'ogit:shortDescription',
            'ogit:soxClass',
            'ogit:startedAt',
            'ogit:status',
            'ogit:subCategory',
            'ogit:subType',
            'ogit:type',
            'ogit:updateCount',
            'ogit:vendor',
            'ogit:version'},
        allowed_connections={
            ('ogit:contains', 'ogit:ConfigurationItem'),
            ('ogit:corresponds', 'ogit.Automation:MARSNode'),
            ('ogit:corresponds', 'ogit.MARS:Application'),
            ('ogit:corresponds', 'ogit.MARS:Machine'),
            ('ogit:corresponds', 'ogit.MARS:Resource'),
            ('ogit:corresponds', 'ogit.MARS:Software'),
            ('ogit:corresponds', 'ogit:Organization'),
            ('ogit:corresponds', 'ogit:Person'),
            ('ogit:deployedTo', 'ogit:ConfigurationItem'),
            ('ogit:manages', 'ogit:ConfigurationItem'),
            ('ogit:provides', 'ogit:ConfigurationItem'),
            ('ogit:relates', 'ogit:Asset'),
            ('ogit:relates', 'ogit:Attachment'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit:ConfigurationItem'),
            ('ogit:relates', 'ogit.Datacenter:Server'),
            ('ogit:relates', 'ogit:Device'),
            ('ogit:relates', 'ogit.MARS:Application'),
            ('ogit:relates', 'ogit.MARS:Machine'),
            ('ogit:relates', 'ogit.MARS:Resource'),
            ('ogit:relates', 'ogit.MARS:Software'),
            ('ogit:runsOn', 'ogit:ConfigurationItem'),
            ('ogit:virtualizes', 'ogit:ConfigurationItem')})
    yield Entity(
        about='ogit:Contract',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:deadline',
            'ogit:description',
            'ogit:expirationDate',
            'ogit:status',
            'ogit:type',
            'ogit:validFrom',
            'ogit:validTo'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:contains', 'ogit:License'),
            ('ogit:contains', 'ogit.ServiceManagement:SLA'),
            ('ogit:defines', 'ogit:Penalty'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Cost:Budget',
        parent='ogit:Node',
        allowed_connections={('ogit:covers', 'ogit.Cost:CostElement')})
    yield Entity(
        about='ogit.Cost:CostDistribution',
        parent='ogit:Node',
        allowed_connections={('ogit:contains', 'ogit.Cost:CostElement')})
    yield Entity(
        about='ogit.Cost:CostElement',
        parent='ogit:Node',
        allowed_connections={('ogit:contributes', 'ogit.Cost:CostDistribution')})
    yield Entity(
        about='ogit.Cost:PlanningParameter',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:assumes', 'ogit.Cost:PlanningTemplate'),
            ('ogit:specifies', 'ogit:Parameter')})
    yield Entity(
        about='ogit.Cost:PlanningTemplate',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:contains', 'ogit.Cost:PlanningTemplate'),
            ('ogit:plans', 'ogit.Automation:MARSModelTemplate'),
            ('ogit:plans', 'ogit.Cost:CostElement')})
    yield Entity(
        about='ogit:Course',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:name'},
        optional_attributes={
            'ogit:creator',
            'ogit:description',
            'ogit:status'})
    yield Entity(
        about='ogit.Credit:Contract',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={
            ('ogit:has', 'ogit.Credit:Instrument'),
            ('ogit:has', 'ogit.Credit:Purpose')})
    yield Entity(
        about='ogit.Credit:Counterparty',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:name',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={
            ('ogit.Credit:credits', 'ogit.Credit:Instrument'),
            ('ogit.Credit:debts', 'ogit.Credit:Instrument'),
            ('ogit.Credit:hasHeadOffice', 'ogit.Credit:Counterparty'),
            ('ogit.Credit:hasImmediateParent', 'ogit.Credit:Counterparty'),
            ('ogit.Credit:hasUltimateParent', 'ogit.Credit:Counterparty'),
            ('ogit.Credit:observes', 'ogit.Credit:Contract'),
            ('ogit.Credit:observes', 'ogit.Credit:CounterpartyMutable'),
            ('ogit.Credit:observes', 'ogit.Credit:Instrument'),
            ('ogit.Credit:observes', 'ogit.Credit:InstrumentMutable'),
            ('ogit.Credit:observes', 'ogit.Credit:Protection'),
            ('ogit.Credit:observes', 'ogit.Credit:ProtectionMutable'),
            ('ogit.Credit:originates', 'ogit.Credit:Instrument'),
            ('ogit.Credit:services', 'ogit.Credit:Instrument'),
            ('ogit:belongs', 'ogit.Credit:EconomicActivity'),
            ('ogit:corresponds', 'ogit.Credit:Counterparty'),
            ('ogit:follows', 'ogit.Credit:Counterparty'),
            ('ogit:has', 'ogit.Credit:JointLiability'),
            ('ogit:locatedAt', 'ogit.Location:Address'),
            ('ogit:provides', 'ogit.Credit:Protection'),
            ('ogit:reports', 'ogit.Credit:Contract'),
            ('ogit:reports', 'ogit.Credit:CounterpartyMutable'),
            ('ogit:reports', 'ogit.Credit:CounterpartyMutable'),
            ('ogit:reports', 'ogit.Credit:Instrument'),
            ('ogit:reports', 'ogit.Credit:InstrumentMutable'),
            ('ogit:reports', 'ogit.Credit:Protection'),
            ('ogit:reports', 'ogit.Credit:ProtectionMutable')})
    yield Entity(
        about='ogit.Credit:CounterpartyMutable',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={('ogit:follows', 'ogit.Credit:CounterpartyMutable')})
    yield Entity(
        about='ogit.Credit:EconomicActivity',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:description',
            'ogit:title'})
    yield Entity(
        about='ogit.Credit:Instrument',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Credit:InstrumentType'),
            ('ogit:follows', 'ogit.Credit:Instrument'),
            ('ogit:reports', 'ogit.Credit:InstrumentMutable')})
    yield Entity(
        about='ogit.Credit:InstrumentMutable',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={('ogit:follows', 'ogit.Credit:InstrumentMutable')})
    yield Entity(
        about='ogit.Credit:InstrumentType',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.Credit:JointLiability',
        parent='ogit:Node',
        required_attributes={'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={('ogit:connects', 'ogit.Credit:Instrument')})
    yield Entity(
        about='ogit.Credit:Protection',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={
            ('ogit.Credit:secures', 'ogit.Credit:Instrument'),
            ('ogit:belongs', 'ogit.Credit:ProtectionType'),
            ('ogit:follows', 'ogit.Credit:Protection'),
            ('ogit:reports', 'ogit.Credit:ProtectionMutable')})
    yield Entity(
        about='ogit.Credit:ProtectionMutable',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:validFrom'},
        optional_attributes={'ogit:validTo'},
        allowed_connections={('ogit:follows', 'ogit.Credit:ProtectionMutable')})
    yield Entity(
        about='ogit.Credit:ProtectionType',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.Credit:Purpose',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit:CustomApplicationData',
        parent='ogit:Node',
        allowed_connections={('ogit:uses', 'ogit:CustomApplicationData')})
    yield Entity(
        about='ogit.CustomerSupport:Comment',
        parent='ogit:Node',
        optional_attributes={
            'ogit.CustomerSupport:htmlContent',
            'ogit.CustomerSupport:metadata',
            'ogit.CustomerSupport:public',
            'ogit.CustomerSupport:remoteId',
            'ogit.CustomerSupport:remoteType',
            'ogit.CustomerSupport:remoteUrl',
            'ogit:content',
            'ogit:createdAt',
            'ogit:id',
            'ogit:type'},
        allowed_connections={
            ('ogit:associates', 'ogit:Attachment'),
            ('ogit:belongs', 'ogit.CustomerSupport:Ticket')})
    yield Entity(
        about='ogit.CustomerSupport:Group',
        parent='ogit:Node',
        optional_attributes={
            'ogit.CustomerSupport:deleted',
            'ogit.CustomerSupport:remoteId',
            'ogit.CustomerSupport:remoteType',
            'ogit.CustomerSupport:remoteUrl',
            'ogit:createdAt',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:name'})
    yield Entity(
        about='ogit.CustomerSupport:Organization',
        parent='ogit:Node',
        optional_attributes={
            'ogit.CustomerSupport:customFieldNames',
            'ogit.CustomerSupport:details',
            'ogit.CustomerSupport:domainNames',
            'ogit.CustomerSupport:note',
            'ogit.CustomerSupport:remoteId',
            'ogit.CustomerSupport:remoteType',
            'ogit.CustomerSupport:remoteUrl',
            'ogit.CustomerSupport:shareComments',
            'ogit.CustomerSupport:shareTickets',
            'ogit.CustomerSupport:tags',
            'ogit:createdAt',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:name'},
        allowed_connections={('ogit:employs', 'ogit.CustomerSupport:Group')})
    yield Entity(
        about='ogit.CustomerSupport:Ticket',
        parent='ogit:Node',
        optional_attributes={
            'ogit.CustomerSupport:allowAttachments',
            'ogit.CustomerSupport:customFieldNames',
            'ogit.CustomerSupport:hasIncidents',
            'ogit.CustomerSupport:recipient',
            'ogit.CustomerSupport:remoteId',
            'ogit.CustomerSupport:remoteType',
            'ogit.CustomerSupport:remoteUrl',
            'ogit.CustomerSupport:tags',
            'ogit:createdAt',
            'ogit:deadline',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:priority',
            'ogit:status',
            'ogit:summary',
            'ogit:type'},
        allowed_connections={
            ('ogit:assignedTo', 'ogit.CustomerSupport:Group'),
            ('ogit:assignedTo', 'ogit.CustomerSupport:User'),
            ('ogit:associates', 'ogit.CustomerSupport:Organization'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:updates', 'ogit.CustomerSupport:User')})
    yield Entity(
        about='ogit.CustomerSupport:User',
        parent='ogit:Node',
        optional_attributes={
            'ogit.CustomerSupport:customFieldNames',
            'ogit.CustomerSupport:defaultGroupId',
            'ogit.CustomerSupport:defaultOrganizationId',
            'ogit.CustomerSupport:details',
            'ogit.CustomerSupport:lastLoginAt',
            'ogit.CustomerSupport:locale',
            'ogit.CustomerSupport:multiFactorAuth',
            'ogit.CustomerSupport:note',
            'ogit.CustomerSupport:privateCommentsOnly',
            'ogit.CustomerSupport:remoteId',
            'ogit.CustomerSupport:remoteType',
            'ogit.CustomerSupport:remoteUrl',
            'ogit.CustomerSupport:restrictedAgent',
            'ogit.CustomerSupport:role',
            'ogit.CustomerSupport:roleType',
            'ogit.CustomerSupport:signature',
            'ogit.CustomerSupport:suspended',
            'ogit.CustomerSupport:tags',
            'ogit.CustomerSupport:ticketRestriction',
            'ogit.CustomerSupport:timeZone',
            'ogit.CustomerSupport:verified',
            'ogit:alternativeName',
            'ogit:createdAt',
            'ogit:email',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:name',
            'ogit:phone',
            'ogit:status'},
        allowed_connections={
            ('ogit.CustomerSupport:collaborates', 'ogit.CustomerSupport:Ticket'),
            ('ogit.CustomerSupport:submits', 'ogit.CustomerSupport:Ticket'),
            ('ogit:belongs', 'ogit.CustomerSupport:Group'),
            ('ogit:belongs', 'ogit.CustomerSupport:Organization'),
            ('ogit:creates', 'ogit.CustomerSupport:Comment'),
            ('ogit:follows', 'ogit.CustomerSupport:Ticket'),
            ('ogit:requests', 'ogit.CustomerSupport:Ticket'),
            ('ogit:subscribes', 'ogit.CustomerSupport:Organization')})
    yield Entity(
        about='ogit.Data:Log',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Data:timeToLive',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.DataProcessing:DataView',
        parent='ogit:Node',
        optional_attributes={
            'ogit.DataProcessing:parameters',
            'ogit.DataProcessing:query',
            'ogit.DataProcessing:queryType',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.DataProcessing:Program',
        parent='ogit:Node',
        required_attributes={
            'ogit.DataProcessing:outputType',
            'ogit.DataProcessing:parameters',
            'ogit.DataProcessing:query',
            'ogit.DataProcessing:queryType',
            'ogit:content'},
        optional_attributes={
            'ogit.DataProcessing:internalJobId',
            'ogit.DataProcessing:state',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.Datacenter:Building',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:datacenterId',
            'ogit:capacity',
            'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Datacenter:Datacenter'),
            ('ogit:contains', 'ogit.Datacenter:Room')})
    yield Entity(
        about='ogit.Datacenter:Cooling',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:roomId',
            'ogit:capacity',
            'ogit:id',
            'ogit:powerConsumption'})
    yield Entity(
        about='ogit.Datacenter:Datacenter',
        parent='ogit:Node',
        optional_attributes={
            'ogit:capacity',
            'ogit:id'},
        allowed_connections={('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit.Datacenter:PowerDistributionUnit',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:rackId',
            'ogit:capacity',
            'ogit:id'})
    yield Entity(
        about='ogit.Datacenter:Rack',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:moveProductionDate',
            'ogit.Datacenter:roomId',
            'ogit:brand',
            'ogit:capacity',
            'ogit:endOfWarranty',
            'ogit:id',
            'ogit:model',
            'ogit:powerConsumption',
            'ogit:purchaseDate',
            'ogit:weight'},
        allowed_connections={
            ('ogit:contains', 'ogit.Datacenter:PowerDistributionUnit'),
            ('ogit:contains', 'ogit.Datacenter:Sensor'),
            ('ogit:contains', 'ogit:Device')})
    yield Entity(
        about='ogit.Datacenter:Room',
        parent='ogit:Node',
        optional_attributes={
            'ogit:buildingId',
            'ogit:capacity',
            'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Datacenter:Cooling'),
            ('ogit:contains', 'ogit.Datacenter:Rack'),
            ('ogit:contains', 'ogit.Datacenter:Section'),
            ('ogit:contains', 'ogit.Datacenter:Sensor')})
    yield Entity(
        about='ogit.Datacenter:Section',
        parent='ogit:Node',
        optional_attributes={
            'ogit:capacity',
            'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Datacenter:Rack'),
            ('ogit:contains', 'ogit.Datacenter:Sensor')})
    yield Entity(
        about='ogit.Datacenter:Sensor',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:sectionId',
            'ogit:id'})
    yield Entity(
        about='ogit.Datacenter:Server',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:moveProductionDate',
            'ogit:brand',
            'ogit:endOfWarranty',
            'ogit:id',
            'ogit:model',
            'ogit:purchaseDate'},
        allowed_connections={
            ('ogit:corresponds', 'ogit:Device'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Datacenter:Storage',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:moveProductionDate',
            'ogit:brand',
            'ogit:endOfWarranty',
            'ogit:id',
            'ogit:model',
            'ogit:purchaseDate'},
        allowed_connections={('ogit:corresponds', 'ogit:Device')})
    yield Entity(
        about='ogit.Datacenter:UPS',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={('ogit:corresponds', 'ogit:Device')})
    yield Entity(
        about='ogit:Device',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Datacenter:moveProductionDate',
            'ogit:endOfWarranty',
            'ogit:id',
            'ogit:name',
            'ogit:powerConsumption',
            'ogit:purchaseDate'},
        allowed_connections={
            ('ogit:connects', 'ogit.Datacenter:PowerDistributionUnit'),
            ('ogit:connects', 'ogit.Datacenter:UPS'),
            ('ogit:contains', 'ogit.Datacenter:Sensor'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Documents:Document',
        parent='ogit:Node',
        optional_attributes={
            'ogit:creationTime',
            'ogit:modificationTime',
            'ogit:name',
            'ogit:type',
            'ogit:version'},
        allowed_connections={('ogit:consistsOf', 'ogit:Attachment')})
    yield Entity(
        about='ogit.Documents:Spreadsheet',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Documents:headers',
            'ogit.Documents:rows',
            'ogit:creationTime',
            'ogit:modificationTime',
            'ogit:name',
            'ogit:type',
            'ogit:version'},
        allowed_connections={
            ('ogit:generates', 'ogit:Attachment'),
            ('ogit:represents', 'ogit:Attachment')})
    yield Entity(
        about='ogit:Email',
        parent='ogit:Node',
        required_attributes={'ogit:status'},
        allowed_connections={('ogit:connects', 'ogit:Person')})
    yield Entity(
        about='ogit:Entity',
        required_attributes={
            'ogit:admin-contact',
            'ogit:parent',
            'ogit:scope',
            'ogit:tech-contact'},
        optional_attributes={
            'ogit:deleter',
            'ogit:hide'})
    yield Entity(
        about='ogit:Environment',
        parent='ogit:Node',
        optional_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:consistsOf', 'ogit.Automation:MARSNode'),
            ('ogit:consistsOf', 'ogit.MARS:Application'),
            ('ogit:utilizes', 'ogit:Product')})
    yield Entity(
        about='ogit:Event',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:name'},
        optional_attributes={
            'ogit.ServiceManagement:reportedSource',
            'ogit:acknowledgeState',
            'ogit:category',
            'ogit:certainty',
            'ogit:description',
            'ogit:expiresAt',
            'ogit:firstOccurredAt',
            'ogit:impact',
            'ogit:instance',
            'ogit:isRoot',
            'ogit:lastClearedAt',
            'ogit:lastOccurredAt',
            'ogit:lastUpdatedAt',
            'ogit:maintenanceState',
            'ogit:occurenceCount',
            'ogit:openedAt',
            'ogit:priority',
            'ogit:resource',
            'ogit:severity',
            'ogit:sourceId',
            'ogit:status',
            'ogit:summary',
            'ogit:type'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit:ConfigurationItem'),
            ('ogit:affects', 'ogit.MARS:Application'),
            ('ogit:affects', 'ogit.MARS:Machine'),
            ('ogit:affects', 'ogit.MARS:Resource'),
            ('ogit:affects', 'ogit.MARS:Software'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:alerts', 'ogit.Auth:Account'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit:Event'),
            ('ogit:relates', 'ogit.MARS:Application'),
            ('ogit:relates', 'ogit.MARS:Machine'),
            ('ogit:relates', 'ogit.MARS:Resource'),
            ('ogit:relates', 'ogit.MARS:Software'),
            ('ogit:relates', 'ogit.ServiceManagement:Incident'),
            ('ogit:relates', 'ogit.ServiceManagement:Order')})
    yield Entity(
        about='ogit.Examples.Crow:Crossing',
        optional_attributes={
            'ogit.Examples.Crow:carLightStatus',
            'ogit.Examples.Crow:pedestrianLightStatus'},
        allowed_connections={('ogit:isPartOf', 'ogit.Examples.Crow:Street')})
    yield Entity(
        about='ogit.Examples.Crow:Food',
        required_attributes={'ogit.Examples.Crow:foodType'},
        optional_attributes={
            'ogit.Examples.Crow:foodAccessible',
            'ogit.Examples.Crow:foodKcal'},
        allowed_connections={
            ('ogit:locatedAt', 'ogit.Examples.Crow:Sidewalk'),
            ('ogit:locatedAt', 'ogit.Examples.Crow:Street'),
            ('ogit:locatedAt', 'ogit.Examples.Crow:Tree')})
    yield Entity(
        about='ogit.Examples.Crow:Scene',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:has', 'ogit.Examples.Crow:Crossing'),
            ('ogit:has', 'ogit.Examples.Crow:Food'),
            ('ogit:has', 'ogit.Examples.Crow:Sidewalk'),
            ('ogit:has', 'ogit.Examples.Crow:Street'),
            ('ogit:has', 'ogit.Examples.Crow:Tree')})
    yield Entity(
        about='ogit.Examples.Crow:Sidewalk',
        optional_attributes={'ogit:name'})
    yield Entity(
        about='ogit.Examples.Crow:Street',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit.Examples.Crow:approachingCars'})
    yield Entity(
        about='ogit.Examples.Crow:Tree',
        optional_attributes={'ogit:name'})
    yield Entity(
        about='ogit.Factory:Action',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:duration',
            'ogit:durationUnit',
            'ogit:frequency',
            'ogit:name',
            'ogit:subType'},
        allowed_connections={
            ('ogit:affects', 'ogit.Factory:Component'),
            ('ogit:affects', 'ogit.Factory:Machine'),
            ('ogit:requires', 'ogit.Factory:Action'),
            ('ogit:responds', 'ogit.Factory:Failure')})
    yield Entity(
        about='ogit.Factory:Component',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Factory:equipmentNumber',
            'ogit:description',
            'ogit:name',
            'ogit:status',
            'ogit:subType'},
        allowed_connections={
            ('ogit:contains', 'ogit.Factory:Component'),
            ('ogit:corresponds', 'ogit.Factory:Component')})
    yield Entity(
        about='ogit.Factory:Factory',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.Factory:hasAl', 'ogit.Factory:ProductionLine'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:uses', 'ogit.Factory:StorageInventory'),
            ('ogit:uses', 'ogit.Factory:StorageTank')})
    yield Entity(
        about='ogit.Factory:Failure',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:severity',
            'ogit:status',
            'ogit:subType'},
        allowed_connections={
            ('ogit:affects', 'ogit.Factory:Component'),
            ('ogit:causes', 'ogit.Factory:Failure')})
    yield Entity(
        about='ogit.Factory:Machine',
        parent='ogit:Node')
    yield Entity(
        about='ogit.Factory:Plant',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:status'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Factory:Factory'),
            ('ogit:contains', 'ogit.Factory:Component'),
            ('ogit:locatedAt', 'ogit:Location')})
    yield Entity(
        about='ogit.Factory:ProductionLine',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:contains', 'ogit.Factory:Machine'),
            ('ogit:produces', 'ogit:Product')})
    yield Entity(
        about='ogit.Factory:StorageInventory',
        parent='ogit:Node')
    yield Entity(
        about='ogit.Factory:StorageTank',
        parent='ogit:Node')
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Invoice',
        optional_attributes={
            'ogit.FinancialAccounting:amount',
            'ogit.FinancialAccounting:invoiceDate',
            'ogit.FinancialAccounting:invoiceNumber',
            'ogit:currency'},
        allowed_connections={
            ('ogit:contains', 'ogit.FinancialAccounting.AccountsPayable:InvoiceLineItem'),
            ('ogit:has', 'ogit:Attachment')})
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:InvoiceLineItem',
        optional_attributes={
            'ogit.FinancialAccounting:amount',
            'ogit.FinancialAccounting:quantity',
            'ogit:positionNumber',
            'ogit:title'})
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Payment',
        optional_attributes={
            'ogit.FinancialAccounting:amount',
            'ogit.FinancialAccounting:transactionDate',
            'ogit.FinancialAccounting:valueDate',
            'ogit:currency',
            'ogit:description'},
        allowed_connections={('ogit:belongs', 'ogit.FinancialAccounting.AccountsPayable:Invoice')})
    yield Entity(
        about='ogit.FinancialAccounting.AccountsPayable:Vendor',
        required_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:corresponds', 'ogit:Organization'),
            ('ogit:has', 'ogit.Location:Address'),
            ('ogit:issues', 'ogit.FinancialAccounting.AccountsPayable:Invoice')})
    yield Entity(
        about='ogit.FinancialAccounting:Company',
        required_attributes={'ogit:name'},
        allowed_connections={('ogit:corresponds', 'ogit:Organization')})
    yield Entity(
        about='ogit.FinancialAccounting:OrganizationalUnit',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit.FinancialAccounting:companyCode'},
        allowed_connections={
            ('ogit:corresponds', 'ogit:Organization'),
            ('ogit:has', 'ogit.Location:Address'),
            ('ogit:isPartOf', 'ogit.FinancialAccounting:Company'),
            ('ogit:receives', 'ogit.Location:Address')})
    yield Entity(
        about='ogit.FinancialMarket:AggregatedContracts',
        parent='ogit:Node',
        required_attributes={'ogit:currency'},
        optional_attributes={
            'ogit.FinancialMarket:issueDate',
            'ogit.FinancialMarket:maturityDate',
            'ogit:description',
            'ogit:title',
            'ogit:value'})
    yield Entity(
        about='ogit.FinancialMarket:Contract',
        parent='ogit:Node',
        required_attributes={
            'ogit:currency',
            'ogit:id'},
        optional_attributes={
            'ogit.FinancialMarket:issueDate',
            'ogit.FinancialMarket:maturityDate',
            'ogit:title',
            'ogit:value'},
        allowed_connections={
            ('ogit.FinancialMarket:securedBy', 'ogit.FinancialMarket:Protection'),
            ('ogit:reports', 'ogit:Timeseries'),
            ('ogit:soldTo', 'ogit.FinancialMarket:Corporation'),
            ('ogit:soldTo', 'ogit.FinancialMarket:Project')})
    yield Entity(
        about='ogit.FinancialMarket:Corporation',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.FinancialMarket:defaultDate',
            'ogit.FinancialMarket:defaultStatus',
            'ogit.FinancialMarket:enterpriseSize',
            'ogit.FinancialMarket:legalEntityIdentifier',
            'ogit.FinancialMarket:legalForm',
            'ogit.FinancialMarket:nationalIdentifier'},
        allowed_connections={
            ('ogit.FinancialMarket:brokers', 'ogit.FinancialMarket:Contract'),
            ('ogit.FinancialMarket:credits', 'ogit.FinancialMarket:Contract'),
            ('ogit.FinancialMarket:services', 'ogit.FinancialMarket:Contract'),
            ('ogit:corresponds', 'ogit:Organization'),
            ('ogit:isPartOf', 'ogit.FinancialMarket:Corporation'),
            ('ogit:issues', 'ogit.FinancialMarket:FinancialInstrument'),
            ('ogit:locatedAt', 'ogit.Location:Address'),
            ('ogit:provides', 'ogit.FinancialMarket:Protection'),
            ('ogit:reports', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.FinancialMarket:Country',
        parent='ogit:Node',
        required_attributes={'ogit:name'})
    yield Entity(
        about='ogit.FinancialMarket:EconomicActivity',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:description',
            'ogit:title'})
    yield Entity(
        about='ogit.FinancialMarket:Exchange',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={('ogit:locatedIn', 'ogit.FinancialMarket:Country')})
    yield Entity(
        about='ogit.FinancialMarket:FinancialInstrument',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.FinancialMarket:ISIN',
            'ogit.FinancialMarket:issueDate',
            'ogit.FinancialMarket:maturityDate',
            'ogit:currency'},
        allowed_connections={
            ('ogit:belongs', 'ogit.FinancialMarket:FinancialInstrumentCategory'),
            ('ogit:defines', 'ogit.FinancialMarket:Contract'),
            ('ogit:listedAt', 'ogit.FinancialMarket:Exchange'),
            ('ogit:references', 'ogit.FinancialMarket:Index'),
            ('ogit:reports', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.FinancialMarket:FinancialInstrumentCategory',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.FinancialMarket:Index',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.FinancialMarket:FinancialInstrument'),
            ('ogit:locatedIn', 'ogit.FinancialMarket:Country'),
            ('ogit:reports', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.FinancialMarket:InstitutionalSector',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:description',
            'ogit:title'})
    yield Entity(
        about='ogit.FinancialMarket:Investment',
        parent='ogit:Node',
        optional_attributes={
            'ogit.FinancialMarket:acquisitionDate',
            'ogit.FinancialMarket:amount',
            'ogit.FinancialMarket:currency',
            'ogit.FinancialMarket:value'},
        allowed_connections={('ogit:contains', 'ogit.FinancialMarket:FinancialInstrument')})
    yield Entity(
        about='ogit.FinancialMarket:Investor',
        parent='ogit:Node',
        optional_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:locatedIn', 'ogit.FinancialMarket:Country'),
            ('ogit:owns', 'ogit.FinancialMarket:Investment')})
    yield Entity(
        about='ogit.FinancialMarket:LineOfBusiness',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:corresponds', 'ogit:Organization'),
            ('ogit:has', 'ogit.FinancialMarket:FinancialInstrumentCategory'),
            ('ogit:isPartOf', 'ogit.FinancialMarket:Corporation'),
            ('ogit:owns', 'ogit.FinancialMarket:Portfolio'),
            ('ogit:sells', 'ogit.FinancialMarket:Contract')})
    yield Entity(
        about='ogit.FinancialMarket:Portfolio',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={
            ('ogit:contains', 'ogit.FinancialMarket:Contract'),
            ('ogit:contains', 'ogit.FinancialMarket:FinancialInstrument')})
    yield Entity(
        about='ogit.FinancialMarket:Project',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.FinancialMarket:Protection',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.FinancialMarket:thirdPartyPriorityClaims',
            'ogit:currency',
            'ogit:description',
            'ogit:title',
            'ogit:value'},
        allowed_connections={
            ('ogit:belongs', 'ogit.FinancialMarket:ProtectionType'),
            ('ogit:locatedAt', 'ogit.Location:Address'),
            ('ogit:reports', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.FinancialMarket:ProtectionType',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit.Forum:Award',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        allowed_connections={('ogit:precedes', 'ogit.Forum:Award')})
    yield Entity(
        about='ogit.Forum:Banner',
        parent='ogit:Node',
        required_attributes={'ogit:content'})
    yield Entity(
        about='ogit.Forum:Configuration',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:configures', 'ogit.Forum:Profile'),
            ('ogit:configures', 'ogit:Organization')})
    yield Entity(
        about='ogit.Forum:FeedEntry',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:precedes', 'ogit.Forum:FeedEntry'),
            ('ogit:relates', 'ogit.Automation:AutomationIssue'),
            ('ogit:relates', 'ogit:Comment'),
            ('ogit:relates', 'ogit.Forum:Award'),
            ('ogit:relates', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:relates', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:relates', 'ogit.Forum:Post'),
            ('ogit:relates', 'ogit.Forum:Profile'),
            ('ogit:relates', 'ogit.Forum:Reply'),
            ('ogit:relates', 'ogit.Forum:Topic'),
            ('ogit:relates', 'ogit.Forum:Workflow'),
            ('ogit:relates', 'ogit.Forum:WorkflowStep'),
            ('ogit:relates', 'ogit.Forum:WorkflowTemplate')})
    yield Entity(
        about='ogit.Forum:Group',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.Forum:features', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:associates', 'ogit.Forum:Role'),
            ('ogit:moderates', 'ogit.Forum:WorkflowStep'),
            ('ogit:owns', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:owns', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:owns', 'ogit.Forum:Topic'),
            ('ogit:worksOn', 'ogit.Forum:WorkflowStep')})
    yield Entity(
        about='ogit.Forum:Invite',
        parent='ogit:Node',
        required_attributes={'ogit:token'},
        allowed_connections={
            ('ogit:corresponds', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:corresponds', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:corresponds', 'ogit.Forum:Topic'),
            ('ogit:requests', 'ogit.Forum:Profile')})
    yield Entity(
        about='ogit.Forum:KnowledgeBundle',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:accessControl'},
        allowed_connections={
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit.Forum:WorkflowStep'),
            ('ogit:connects', 'ogit:Hyperlink'),
            ('ogit:contains', 'ogit.Automation:AutomationIssue'),
            ('ogit:contains', 'ogit.Automation:KnowledgeItem'),
            ('ogit:requires', 'ogit.Forum:Permission')})
    yield Entity(
        about='ogit.Forum:KnowledgeBundleHistory',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:accessControl'},
        allowed_connections={
            ('ogit:contains', 'ogit.Automation:AutomationIssue'),
            ('ogit:contains', 'ogit.Automation:KnowledgeItem'),
            ('ogit:relates', 'ogit.Forum:KnowledgeBundle')})
    yield Entity(
        about='ogit.Forum:KnowledgeItemHistory',
        parent='ogit:Node',
        required_attributes={
            'ogit.Automation:deployToEngine',
            'ogit.Automation:knowledgeItemFormalRepresentation'},
        optional_attributes={
            'ogit.Automation:knowledgeItemTier',
            'ogit:accessControl',
            'ogit:changeLog',
            'ogit:creationTime',
            'ogit:description',
            'ogit:isValid',
            'ogit:modificationTime',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:associates', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit.Forum:WorkflowStep'),
            ('ogit:connects', 'ogit:Hyperlink'),
            ('ogit:relates', 'ogit.Automation:KnowledgeItem'),
            ('ogit:requires', 'ogit.Forum:Permission')})
    yield Entity(
        about='ogit.Forum:Permission',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:approves', 'ogit.Forum:Group'),
            ('ogit:approves', 'ogit.Forum:Profile'),
            ('ogit:approves', 'ogit:Organization')})
    yield Entity(
        about='ogit.Forum:Post',
        parent='ogit:Node',
        required_attributes={'ogit:content'},
        allowed_connections={
            ('ogit.Forum:mentions', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit.Forum:WorkflowStep'),
            ('ogit:connects', 'ogit:Hyperlink')})
    yield Entity(
        about='ogit.Forum:Profile',
        parent='ogit:Node',
        required_attributes={
            'ogit.Forum:username',
            'ogit:name'},
        allowed_connections={
            ('ogit.Forum:downloads', 'ogit.Automation:KnowledgeItem'),
            ('ogit.Forum:downloads', 'ogit.Forum:KnowledgeBundle'),
            ('ogit.Forum:downloads', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit.Forum:mentions', 'ogit.Forum:Profile'),
            ('ogit.Forum:rates', 'ogit.Forum:Rating'),
            ('ogit:accepts', 'ogit.Forum:Invite'),
            ('ogit:belongs', 'ogit.Forum:Group'),
            ('ogit:belongs', 'ogit:Person'),
            ('ogit:belongs', 'ogit:Person'),
            ('ogit:creates', 'ogit:Attachment'),
            ('ogit:creates', 'ogit.Automation:AutomationIssue'),
            ('ogit:creates', 'ogit.Automation:KnowledgeItem'),
            ('ogit:creates', 'ogit:Comment'),
            ('ogit:creates', 'ogit.Forum:Invite'),
            ('ogit:creates', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:creates', 'ogit.Forum:KnowledgeBundleHistory'),
            ('ogit:creates', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:creates', 'ogit.Forum:Permission'),
            ('ogit:creates', 'ogit.Forum:Post'),
            ('ogit:creates', 'ogit.Forum:Rating'),
            ('ogit:creates', 'ogit.Forum:Reply'),
            ('ogit:creates', 'ogit.Forum:Review'),
            ('ogit:creates', 'ogit.Forum:Topic'),
            ('ogit:creates', 'ogit.Forum:Workflow'),
            ('ogit:creates', 'ogit.Forum:WorkflowTemplate'),
            ('ogit:endorses', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:endorses', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:endorses', 'ogit.Forum:Post'),
            ('ogit:endorses', 'ogit.Forum:Rating'),
            ('ogit:endorses', 'ogit.Forum:Reply'),
            ('ogit:moderates', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:moderates', 'ogit.Forum:Topic'),
            ('ogit:owns', 'ogit.Forum:FeedEntry'),
            ('ogit:owns', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:owns', 'ogit.Forum:Topic'),
            ('ogit:owns', 'ogit:Notification'),
            ('ogit:rejects', 'ogit.Forum:Invite'),
            ('ogit:subscribes', 'ogit.Forum:FeedEntry'),
            ('ogit:subscribes', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:subscribes', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:subscribes', 'ogit.Forum:Post'),
            ('ogit:subscribes', 'ogit.Forum:Profile'),
            ('ogit:subscribes', 'ogit.Forum:Topic'),
            ('ogit:wins', 'ogit.Forum:Award')})
    yield Entity(
        about='ogit.Forum:Rating',
        parent='ogit:Node',
        required_attributes={'ogit:value'},
        optional_attributes={'ogit:content'},
        allowed_connections={
            ('ogit.Forum:rates', 'ogit.Automation:KnowledgeItem'),
            ('ogit.Forum:rates', 'ogit.Forum:KnowledgeBundle'),
            ('ogit.Forum:rates', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:belongs', 'ogit.Forum:Reply')})
    yield Entity(
        about='ogit.Forum:Reply',
        parent='ogit:Node',
        required_attributes={'ogit:content'},
        allowed_connections={
            ('ogit.Forum:mentions', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit:Comment'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Forum:Profile'),
            ('ogit:connects', 'ogit.Forum:Reply'),
            ('ogit:connects', 'ogit.Forum:Topic'),
            ('ogit:connects', 'ogit:Hyperlink'),
            ('ogit:relates', 'ogit:Attachment'),
            ('ogit:relates', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:relates', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:relates', 'ogit.Forum:Post'),
            ('ogit:responds', 'ogit:Attachment'),
            ('ogit:responds', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:responds', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:responds', 'ogit.Forum:Post'),
            ('ogit:responds', 'ogit.Forum:Rating'),
            ('ogit:responds', 'ogit.Forum:Reply'),
            ('ogit:responds', 'ogit.Forum:WorkflowStep')})
    yield Entity(
        about='ogit.Forum:Review',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:approves', 'ogit.Forum:WorkflowStep'),
            ('ogit:belongs', 'ogit.Forum:Reply'),
            ('ogit:rejects', 'ogit.Forum:WorkflowStep')})
    yield Entity(
        about='ogit.Forum:Role',
        parent='ogit:Node',
        allowed_connections={('ogit:belongs', 'ogit.Forum:Profile')})
    yield Entity(
        about='ogit.Forum:ShortId',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={'ogit:function'},
        allowed_connections={
            ('ogit:specifies', 'ogit.Automation:KnowledgeItem'),
            ('ogit:specifies', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:specifies', 'ogit.Forum:Post')})
    yield Entity(
        about='ogit.Forum:Tag',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:assignedTo', 'ogit.Automation:KnowledgeItem'),
            ('ogit:assignedTo', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:assignedTo', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:assignedTo', 'ogit.Forum:Post'),
            ('ogit:assignedTo', 'ogit.Forum:Reply'),
            ('ogit:assignedTo', 'ogit.Forum:Topic'),
            ('ogit:assignedTo', 'ogit.Forum:WorkflowStep')})
    yield Entity(
        about='ogit.Forum:Topic',
        parent='ogit:Node',
        required_attributes={
            'ogit:description',
            'ogit:title'},
        optional_attributes={'ogit:accessControl'},
        allowed_connections={
            ('ogit:contains', 'ogit.Forum:Post'),
            ('ogit:requires', 'ogit.Forum:Permission')})
    yield Entity(
        about='ogit.Forum:Workflow',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:connects', 'ogit.Automation:AutomationIssue'),
            ('ogit:contains', 'ogit.Forum:FeedEntry'),
            ('ogit:defines', 'ogit.Forum:WorkflowStep'),
            ('ogit:owns', 'ogit.Forum:Group'),
            ('ogit:worksOn', 'ogit.Forum:WorkflowStep')})
    yield Entity(
        about='ogit.Forum:WorkflowStep',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        allowed_connections={
            ('ogit:assignedTo', 'ogit.Forum:Profile'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:connects', 'ogit:Attachment'),
            ('ogit:connects', 'ogit.Automation:KnowledgeItem'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundle'),
            ('ogit:connects', 'ogit.Forum:KnowledgeBundleHistory'),
            ('ogit:connects', 'ogit.Forum:KnowledgeItemHistory'),
            ('ogit:connects', 'ogit.Forum:Post'),
            ('ogit:connects', 'ogit.Knowledge:AcquisitionSession'),
            ('ogit:requires', 'ogit.Forum:Permission')})
    yield Entity(
        about='ogit.Forum:WorkflowTemplate',
        parent='ogit:Node',
        required_attributes={'ogit:title'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:defines', 'ogit.Forum:WorkflowStep'),
            ('ogit:owns', 'ogit.Forum:Group')})
    yield Entity(
        about='ogit.HR.Recruiting:Applicant',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.HR.Recruiting:appliesFor', 'ogit:Role'),
            ('ogit.HR.Recruiting:submits', 'ogit.HR.Recruiting:Resume')})
    yield Entity(
        about='ogit.HR.Recruiting:Education',
        parent='ogit:Node')
    yield Entity(
        about='ogit.HR.Recruiting:Recruiter',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.HR.Recruiting:recruitsFor', 'ogit:Role'),
            ('ogit.HR.Recruiting:worksFor', 'ogit:Organization'),
            ('ogit:has', 'ogit.Auth:Account'),
            ('ogit:reviews', 'ogit.HR.Recruiting:Resume')})
    yield Entity(
        about='ogit.HR.Recruiting:Relevance',
        parent='ogit:Node',
        allowed_connections={('ogit:prioritizes', 'ogit.HR.Recruiting:Skill')})
    yield Entity(
        about='ogit.HR.Recruiting:Resume',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:contains', 'ogit.HR.Recruiting:Education'),
            ('ogit:contains', 'ogit.HR.Recruiting:Skill'),
            ('ogit:contains', 'ogit.HR.Recruiting:WorkHistory'),
            ('ogit:has', 'ogit.HR.Recruiting:Score')})
    yield Entity(
        about='ogit.HR.Recruiting:RoleTitle',
        parent='ogit:Node',
        allowed_connections={('ogit:belongs', 'ogit:Role')})
    yield Entity(
        about='ogit.HR.Recruiting:Score',
        parent='ogit:Node',
        allowed_connections={('ogit:belongs', 'ogit:Role')})
    yield Entity(
        about='ogit.HR.Recruiting:Skill',
        parent='ogit:Node',
        optional_attributes={'ogit:category'},
        allowed_connections={('ogit:belongs', 'ogit.HR.Recruiting:SkillGroup')})
    yield Entity(
        about='ogit.HR.Recruiting:SkillGroup',
        parent='ogit:Node')
    yield Entity(
        about='ogit.HR.Recruiting:WorkHistory',
        parent='ogit:Node',
        allowed_connections={('ogit:contains', 'ogit.HR.Recruiting:RoleTitle')})
    yield Entity(
        about='ogit.Health.Diagnostics:Anamnesis',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Health.Diagnostics:appID',
            'ogit.Health.Diagnostics:symptoms',
            'ogit.Mobile:appVersion',
            'ogit.Mobile:deviceModel',
            'ogit.Mobile:devicePlatform',
            'ogit.Mobile:osVersion',
            'ogit:gender',
            'ogit:latitude',
            'ogit:locationAcquisitionTime',
            'ogit:locationPrecision',
            'ogit:longitude',
            'ogit:manufacturer',
            'ogit:yearOfBirth'})
    yield Entity(
        about='ogit.Health.Diagnostics:Demographics',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Health.Diagnostics:birthyearRange',
            'ogit.Health.Diagnostics:symptoms',
            'ogit.Location:residenceCountry',
            'ogit.Location:zipCode',
            'ogit:gender',
            'ogit:latitude',
            'ogit:longitude'})
    yield Entity(
        about='ogit.Health.Diagnostics:Equipment',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Health.Diagnostics:batteryLevel',
            'ogit.Health.Diagnostics:batteryState',
            'ogit.Health.Diagnostics:equipmentID',
            'ogit.Health.Diagnostics:equipmentState',
            'ogit.Health.Diagnostics:equipmentStateChangeTime',
            'ogit.Health.Diagnostics:firmwareVersion',
            'ogit.Mobile:activationTime',
            'ogit.Mobile:deviceModel'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Health.Diagnostics:TestStation'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:performs', 'ogit.Health.Diagnostics:Test')})
    yield Entity(
        about='ogit.Health.Diagnostics:Laboratory',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:city',
            'ogit:country',
            'ogit:description',
            'ogit:email',
            'ogit:function',
            'ogit:phone',
            'ogit:postalCode',
            'ogit:streetAddress',
            'ogit:webPage'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:manages', 'ogit.Health.Diagnostics:Equipment'),
            ('ogit:performs', 'ogit.Health.Diagnostics:Test')})
    yield Entity(
        about='ogit.Health.Diagnostics:Test',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Health.Diagnostics:ICDCode',
            'ogit.Health.Diagnostics:appID',
            'ogit.Health.Diagnostics:equipmentID',
            'ogit.Health.Diagnostics:errorCode',
            'ogit.Health.Diagnostics:firmwareVersion',
            'ogit.Health.Diagnostics:liquidContactTime',
            'ogit.Health.Diagnostics:sensorID',
            'ogit.Health.Diagnostics:testCompletedAt',
            'ogit.Health.Diagnostics:testDate',
            'ogit.Health.Diagnostics:testMethod',
            'ogit.Health.Diagnostics:testResult',
            'ogit.Health.Diagnostics:testStartedAt',
            'ogit.Mobile:appVersion'},
        allowed_connections={
            ('ogit:describes', 'ogit:Person'),
            ('ogit:generates', 'ogit:Attachment'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:includes', 'ogit.Health.Diagnostics:Anamnesis'),
            ('ogit:includes', 'ogit.Health.Diagnostics:Demographics')})
    yield Entity(
        about='ogit.Health.Diagnostics:TestStation',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:status'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:locatedAt', 'ogit.Location:Address'),
            ('ogit:performs', 'ogit.Health.Diagnostics:Test')})
    yield Entity(
        about='ogit:Hyperlink',
        parent='ogit:Node',
        required_attributes={'ogit:url'},
        optional_attributes={'ogit:title'})
    yield Entity(
        about='ogit:Installation',
        parent='ogit:Node',
        required_attributes={'ogit:_xid'},
        optional_attributes={
            'ogit:creator',
            'ogit:description',
            'ogit:status'},
        allowed_connections={('ogit:belongs', 'ogit:Organization')})
    yield Entity(
        about='ogit.Knowledge:AcquisitionRoom',
        parent='ogit:Node',
        allowed_connections={('ogit:contains', 'ogit:Comment')})
    yield Entity(
        about='ogit.Knowledge:AcquisitionSession',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Knowledge:archived',
            'ogit:description',
            'ogit:title'},
        indexed_attributes={
            'ogit:description',
            'ogit:title'},
        allowed_connections={
            ('ogit:contains', 'ogit:Comment'),
            ('ogit:contains', 'ogit.Knowledge:AcquisitionRoom'),
            ('ogit:defines', 'ogit.Automation:KnowledgeItem'),
            ('ogit:defines', 'ogit.Knowledge:Step')})
    yield Entity(
        about='ogit.Knowledge:Step',
        parent='ogit:Node')
    yield Entity(
        about='ogit:License',
        parent='ogit:Node',
        optional_attributes={
            'ogit:createdAt',
            'ogit:creator',
            'ogit:deadline',
            'ogit:expirationDate',
            'ogit:id',
            'ogit:licenseKey',
            'ogit:licenseType',
            'ogit:subject',
            'ogit:validFrom',
            'ogit:validTo'},
        allowed_connections={
            ('ogit:associates', 'ogit:Installation'),
            ('ogit:belongs', 'ogit:LicenseRequest'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:precedes', 'ogit:License')})
    yield Entity(
        about='ogit:LicenseRequest',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:creator',
            'ogit:description',
            'ogit:licenseId',
            'ogit:licenseRequestStatus',
            'ogit:licenseType',
            'ogit:subject',
            'ogit:token'},
        allowed_connections={('ogit:belongs', 'ogit:Organization')})
    yield Entity(
        about='ogit:LicenseToken',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:licenseTokenStatus',
            'ogit:description',
            'ogit:expirationDate',
            'ogit:licenseType',
            'ogit:token',
            'ogit:validFrom'},
        allowed_connections={('ogit:belongs', 'ogit:Organization')})
    yield Entity(
        about='ogit:Location',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:description'},
        allowed_connections={
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:locatedIn', 'ogit:Region')})
    yield Entity(
        about='ogit.Location:Address',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.Location:city',
            'ogit.Location:country',
            'ogit.Location:state',
            'ogit.Location:streetName',
            'ogit.Location:streetNumber',
            'ogit.Location:zipCode'})
    yield Entity(
        about='ogit.Location:NUTSLevel1',
        required_attributes={'ogit:name'})
    yield Entity(
        about='ogit.Location:NUTSLevel2',
        required_attributes={'ogit:name'},
        allowed_connections={('ogit:locatedIn', 'ogit.Location:NUTSLevel1')})
    yield Entity(
        about='ogit.Location:NUTSLevel3',
        required_attributes={'ogit:name'},
        allowed_connections={('ogit:locatedIn', 'ogit.Location:NUTSLevel2')})
    yield Entity(
        about='ogit.MARS:Application',
        parent='ogit:Node',
        required_attributes={
            'ogit.MARS.Application:class',
            'ogit.MARS.Application:subClass',
            'ogit:name'},
        optional_attributes={
            'ogit.Automation:automationState',
            'ogit.Automation:lifecycle',
            'ogit.Automation:marsNodeType',
            'ogit.Automation:serviceStatus'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:dependsOn', 'ogit.MARS:Resource'),
            ('ogit:generates', 'ogit.Data:Log'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:relates', 'ogit:License')})
    yield Entity(
        about='ogit.MARS:Machine',
        parent='ogit:Node',
        required_attributes={
            'ogit.MARS.Machine:class',
            'ogit:name'},
        optional_attributes={
            'ogit.Automation:automationState',
            'ogit.Automation:lifecycle',
            'ogit.Automation:marsNodeType',
            'ogit.Automation:serviceStatus',
            'ogit.MARS.Machine:cpuArch',
            'ogit.MARS.Machine:distroName',
            'ogit.MARS.Machine:kernel',
            'ogit.MARS.Machine:ram',
            'ogit.MARS.Network:defaultGateway',
            'ogit.MARS.Network:fqdn',
            'ogit.MARS.Network:interfaceIP',
            'ogit.MARS.Network:interfaceMAC',
            'ogit.MARS.Network:interfaceName',
            'ogit.MARS.Network:interfacePrefixLength',
            'ogit.MARS.Network:ipVersion',
            'ogit.Version:major',
            'ogit.Version:minor',
            'ogit.Version:patch',
            'ogit:endOfWarranty',
            'ogit:serialNumber',
            'ogit:vendor'},
        indexed_attributes={
            'ogit.MARS.Network:fqdn',
            'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:NetworkInterface'),
            ('ogit:generates', 'ogit.Data:Log'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.MARS:Resource',
        parent='ogit:Node',
        required_attributes={
            'ogit.MARS.Resource:class',
            'ogit:name'},
        optional_attributes={
            'ogit.Automation:automationState',
            'ogit.Automation:lifecycle',
            'ogit.Automation:marsNodeType',
            'ogit.Automation:serviceStatus',
            'ogit:url'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:dependsOn', 'ogit.MARS:Software'),
            ('ogit:generates', 'ogit.Data:Log'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:uses', 'ogit.Automation:Configuration')})
    yield Entity(
        about='ogit.MARS:Software',
        parent='ogit:Node',
        required_attributes={
            'ogit.MARS.Software:class',
            'ogit.MARS.Software:subClass',
            'ogit:name'},
        optional_attributes={
            'ogit.Automation:automationState',
            'ogit.Automation:lifecycle',
            'ogit.Automation:marsNodeType',
            'ogit.Automation:serviceStatus',
            'ogit.MARS.Network:bindAddress',
            'ogit.MARS.Network:port',
            'ogit.MARS.Network:protocol',
            'ogit.MARS.Software:installPath',
            'ogit.MARS.Software:installPath',
            'ogit.MARS.Software:instanceId',
            'ogit.MARS.Software:logPath',
            'ogit.MARS.Software:serviceName',
            'ogit.Version:major',
            'ogit.Version:minor',
            'ogit.Version:patch',
            'ogit:endOfWarranty',
            'ogit:serialNumber',
            'ogit:url',
            'ogit:vendor'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:dependsOn', 'ogit.MARS:Machine'),
            ('ogit:generates', 'ogit.Data:Log'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.ML:PredictionModel',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.ML:activeVersion',
            'ogit.ML:attributesSchema',
            'ogit.ML:endpoint',
            'ogit:description'},
        allowed_connections={
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:has', 'ogit.ML:TrainingData'),
            ('ogit:uses', 'ogit.ML:TrainedModel')})
    yield Entity(
        about='ogit.ML:TrainedModel',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.ML:meta',
            'ogit.ML:requirements',
            'ogit.ML:trainedFrom',
            'ogit.ML:trainingSummary',
            'ogit:attachmentID',
            'ogit:status'},
        allowed_connections={
            ('ogit.ML:trainedOn', 'ogit.ML:TrainingData'),
            ('ogit:contains', 'ogit:Attachment')})
    yield Entity(
        about='ogit.ML:TrainingData',
        optional_attributes={
            'ogit.ML:size',
            'ogit.ML:trainData',
            'ogit:attachmentID',
            'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit:Attachment')})
    yield Entity(
        about='ogit.MRO.Aviation:Aircraft',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:locatedIn', 'ogit.MRO.Aviation:Bay')})
    yield Entity(
        about='ogit.MRO.Aviation:AircraftType',
        parent='ogit:Node',
        allowed_connections={('ogit.MRO.Aviation:characterize', 'ogit.MRO.Aviation:Aircraft')})
    yield Entity(
        about='ogit.MRO.Aviation:Airport',
        parent='ogit:Node',
        allowed_connections={('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit.MRO.Aviation:Bay',
        parent='ogit:Node',
        allowed_connections={('ogit:belongs', 'ogit.MRO.Aviation:Facility')})
    yield Entity(
        about='ogit.MRO.Aviation:Capability',
        parent='ogit:Node',
        allowed_connections={('ogit.MRO.Aviation:suppliedBy', 'ogit:Person')})
    yield Entity(
        about='ogit.MRO.Aviation:Component',
        parent='ogit:Node',
        allowed_connections={('ogit.MRO.Aviation:suit', 'ogit.MRO.Aviation:AircraftType')})
    yield Entity(
        about='ogit.MRO.Aviation:Facility',
        parent='ogit:Node')
    yield Entity(
        about='ogit.MRO.Aviation:Layover',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        indexed_attributes={'ogit:name'},
        allowed_connections={('ogit.MRO.Aviation:overhaul', 'ogit.MRO.Aviation:Aircraft')})
    yield Entity(
        about='ogit.MRO.Aviation:MPD',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:id',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit.MRO.Aviation:alternatesWith', 'ogit.MRO.Aviation:MPD'),
            ('ogit.MRO.Aviation:conflictsWith', 'ogit.MRO.Aviation:MPD'),
            ('ogit.MRO.Aviation:references', 'ogit.MRO.Aviation:MPD'),
            ('ogit:includes', 'ogit.MRO.Aviation:MPD'),
            ('ogit:requires', 'ogit.MRO.Aviation:MPD')})
    yield Entity(
        about='ogit.MRO.Aviation:Task',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit.MRO.Aviation:linksTo', 'ogit.MRO.Aviation:AircraftType'),
            ('ogit.MRO.Aviation:performedAt', 'ogit.MRO.Aviation:Workstation'),
            ('ogit.MRO.Aviation:references', 'ogit.MRO.Aviation:MPD'),
            ('ogit:affects', 'ogit.MRO.Aviation:Component'),
            ('ogit:relates', 'ogit.MRO.Aviation:Layover'),
            ('ogit:requires', 'ogit.MRO.Aviation:Capability')})
    yield Entity(
        about='ogit.MRO.Aviation:Workstation',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:locatedIn', 'ogit.MRO.Aviation:Bay'),
            ('ogit:worksOn', 'ogit.MRO.Aviation:Aircraft')})
    yield Entity(
        about='ogit.MRP:Disposet',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:alerts', 'ogit:Alert'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:belongs', 'ogit.MRP:PSG'),
            ('ogit:belongs', 'ogit.MRP:Part'),
            ('ogit:contains', 'ogit:Comment'),
            ('ogit:generates', 'ogit.MRP:Measure')})
    yield Entity(
        about='ogit.MRP:Manufacturer',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.MRP:manufacture', 'ogit.MRP:Part'),
            ('ogit:relates', 'ogit:Organization')})
    yield Entity(
        about='ogit.MRP:Measure',
        parent='ogit:Node',
        allowed_connections={('ogit.MRP:historicised', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.MRP:NormItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit.MRP:actionPeriod1',
            'ogit.MRP:actionPeriod2',
            'ogit.MRP:containerConditions',
            'ogit.MRP:genericNorm',
            'ogit.MRP:kindOfMaterialDetailed',
            'ogit.MRP:kindOfMaterialGeneric',
            'ogit.MRP:kzTCond',
            'ogit.MRP:minimumRemainingShelfLife',
            'ogit.MRP:roomConditions',
            'ogit.MRP:specificNorm',
            'ogit.MRP:tempMax',
            'ogit.MRP:tempMin',
            'ogit.MRP:tempRef',
            'ogit.MRP:totalShelfLife',
            'ogit.MRP:unitOfShelfLife',
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.MRP:PSG',
        parent='ogit:Node')
    yield Entity(
        about='ogit.MRP:Part',
        parent='ogit:Node',
        optional_attributes={
            'ogit.MRP:industryStandard',
            'ogit.MRP:partNumber',
            'ogit:description'},
        allowed_connections={
            ('ogit:complies', 'ogit.MRP:NormItem'),
            ('ogit:consistsOf', 'ogit.MRP:Part')})
    yield Entity(
        about='ogit.MRP:Store',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.MRP:supply', 'ogit.MRP:Disposet'),
            ('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit.MRP:Threshold',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.MRP:applies', 'ogit.MRP:Measure'),
            ('ogit:relates', 'ogit.MRP:Threshold')})
    yield Entity(
        about='ogit.MRP:Vorgang',
        parent='ogit:Node',
        allowed_connections={
            ('ogit:concludes', 'ogit:Organization'),
            ('ogit:contains', 'ogit.MRP:Part')})
    yield Entity(
        about='ogit.MRP:Workshop',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.MRP:performs', 'ogit.MRP:Vorgang'),
            ('ogit:belongs', 'ogit.MRO.Aviation:Facility'),
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit.Mobile:AppInstance',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:appConfigMode',
            'ogit.Mobile:appPermissions',
            'ogit.Mobile:appVersion',
            'ogit.Mobile:bundleID',
            'ogit.Mobile:deviceCodeName',
            'ogit.Mobile:deviceModel',
            'ogit.Mobile:devicePlatform',
            'ogit.Mobile:deviceType',
            'ogit.Mobile:firebaseToken',
            'ogit.Mobile:lastActive',
            'ogit.Mobile:osRadio',
            'ogit.Mobile:osVersion',
            'ogit.Mobile:registrationType',
            'ogit.Mobile:uuid',
            'ogit:consentLevel',
            'ogit:description',
            'ogit:manufacturer'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:connects', 'ogit.Health.Diagnostics:Test'),
            ('ogit:generates', 'ogit.Health.Diagnostics:Demographics'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:has', 'ogit.Auth:Account'),
            ('ogit:has', 'ogit.Mobile:Encounter')})
    yield Entity(
        about='ogit.Mobile:DeviceSpecifications',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:RSSIcorrection',
            'ogit.Mobile:TXcorrection',
            'ogit.Mobile:deviceCodeName',
            'ogit.Mobile:deviceModel',
            'ogit.Mobile:devicePlatform',
            'ogit.Mobile:osRadio',
            'ogit:manufacturer',
            'ogit:source'})
    yield Entity(
        about='ogit.Mobile:Encounter',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:category',
            'ogit.Mobile:criticality',
            'ogit.Mobile:distance',
            'ogit.Mobile:duration',
            'ogit.Mobile:movementType',
            'ogit.Mobile:riskScore',
            'ogit.Mobile:time'})
    yield Entity(
        about='ogit.Mobile:HealthInfo',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:deviceType',
            'ogit.Mobile:healthStatus',
            'ogit.Mobile:healthStatusUpdateTime',
            'ogit.Mobile:label',
            'ogit.Mobile:licenceCode'},
        indexed_attributes={
            'ogit.Mobile:label',
            'ogit.Mobile:licenceCode'})
    yield Entity(
        about='ogit.Mobile:LicenceCodes',
        parent='ogit:Node',
        required_attributes={'ogit.Mobile:licenceCode'},
        optional_attributes={
            'ogit.Mobile:activationTime',
            'ogit.Mobile:deactivationTime',
            'ogit.Mobile:deviceCode',
            'ogit.Mobile:deviceType',
            'ogit.Mobile:isActive',
            'ogit.Mobile:label',
            'ogit.Mobile:lastActive',
            'ogit.Mobile:licenceCode'},
        indexed_attributes={
            'ogit.Mobile:deviceCode',
            'ogit.Mobile:label',
            'ogit.Mobile:licenceCode'})
    yield Entity(
        about='ogit.Mobile:Message',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:delivered',
            'ogit.Mobile:enctime',
            'ogit:name'})
    yield Entity(
        about='ogit.Mobile:MsgTemplate',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Mobile:cta',
            'ogit.Mobile:ctaTarget',
            'ogit.Mobile:ctaType',
            'ogit.Mobile:headline',
            'ogit.Mobile:locale',
            'ogit.Mobile:message',
            'ogit.Mobile:subline',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:AccessControlList',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={('ogit:complies', 'ogit.Network:NetworkSetting')})
    yield Entity(
        about='ogit.Network:FCHBA',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:IDSIPS',
        parent='ogit:Node',
        optional_attributes={'ogit:id'})
    yield Entity(
        about='ogit.Network:IPAddress',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Network:Subnet'),
            ('ogit:relates', 'ogit.Network:NetworkInterface')})
    yield Entity(
        about='ogit.Network:Loadbalancer',
        parent='ogit:Node',
        optional_attributes={'ogit:id'})
    yield Entity(
        about='ogit.Network:MACAddress',
        parent='ogit:Node',
        optional_attributes={'ogit:id'})
    yield Entity(
        about='ogit.Network:NIC',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:MACAddress'),
            ('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:NetworkCard',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:Port'),
            ('ogit:corresponds', 'ogit:Asset'),
            ('ogit:extends', 'ogit.Network:IDSIPS'),
            ('ogit:extends', 'ogit.Network:Loadbalancer'),
            ('ogit:extends', 'ogit.Network:Router'),
            ('ogit:extends', 'ogit.Network:Slot'),
            ('ogit:extends', 'ogit.Network:Switch'),
            ('ogit:extends', 'ogit.Network:WifiAccessPoint')})
    yield Entity(
        about='ogit.Network:NetworkElement',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name',
            'ogit:subType'},
        allowed_connections={('ogit:locatedAt', 'ogit.Network:Site')})
    yield Entity(
        about='ogit.Network:NetworkEnclosure',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:Shelf'),
            ('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:NetworkEndpoint',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:FCHBA'),
            ('ogit:contains', 'ogit.Network:NetworkInterface'),
            ('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:NetworkFabric',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:NetworkCard'),
            ('ogit:contains', 'ogit.Network:SimpleDevice'),
            ('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:NetworkFilter',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={('ogit:complies', 'ogit.Network:NetworkSetting')})
    yield Entity(
        about='ogit.Network:NetworkInterface',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={('ogit:complies', 'ogit.Network:NetworkSetting')})
    yield Entity(
        about='ogit.Network:NetworkLink',
        parent='ogit:Node',
        optional_attributes={
            'ogit:capacity',
            'ogit:id',
            'ogit:subType'},
        allowed_connections={
            ('ogit:connects', 'ogit.Network:NetworkElement'),
            ('ogit:connects', 'ogit.Network:NetworkInterface'),
            ('ogit:connects', 'ogit.Network:Site')})
    yield Entity(
        about='ogit.Network:NetworkSetting',
        parent='ogit:Node',
        optional_attributes={'ogit:id'})
    yield Entity(
        about='ogit.Network:Port',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Network:VLAN'),
            ('ogit:connects', 'ogit.Network:FCHBA'),
            ('ogit:connects', 'ogit.Network:NIC'),
            ('ogit:relates', 'ogit.Network:NetworkInterface')})
    yield Entity(
        about='ogit.Network:PortChannel',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Network:Port'),
            ('ogit:relates', 'ogit.Network:NetworkInterface')})
    yield Entity(
        about='ogit.Network:Router',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:Shelf',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:Slot'),
            ('ogit:corresponds', 'ogit:Asset')})
    yield Entity(
        about='ogit.Network:SimpleDevice',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit.Network:Port'),
            ('ogit:corresponds', 'ogit:Asset'),
            ('ogit:extends', 'ogit.Network:IDSIPS'),
            ('ogit:extends', 'ogit.Network:Loadbalancer'),
            ('ogit:extends', 'ogit.Network:Router'),
            ('ogit:extends', 'ogit.Network:Switch'),
            ('ogit:extends', 'ogit.Network:WifiAccessPoint'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.Network:Site',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'},
        allowed_connections={('ogit:locatedIn', 'ogit.Location:NUTSLevel3')})
    yield Entity(
        about='ogit.Network:Slot',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:Subnet',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:Switch',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:VLAN',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit.Network:WifiAccessPoint',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name'})
    yield Entity(
        about='ogit:Node',
        required_attributes={
            'ogit:_content',
            'ogit:_created-on',
            'ogit:_creator',
            'ogit:_deleted-on',
            'ogit:_edge-id',
            'ogit:_graphtype',
            'ogit:_id',
            'ogit:_is-deleted',
            'ogit:_modified-by',
            'ogit:_modified-on',
            'ogit:_owner',
            'ogit:_tags',
            'ogit:_type',
            'ogit:_version'})
    yield Entity(
        about='ogit:Note',
        parent='ogit:Node',
        optional_attributes={
            'ogit:content',
            'ogit:name'})
    yield Entity(
        about='ogit:Notification',
        parent='ogit:Node',
        optional_attributes={
            'ogit:category',
            'ogit:condition',
            'ogit:description',
            'ogit:expiresAt',
            'ogit:firstOccurredAt',
            'ogit:lastOccurredAt',
            'ogit:message',
            'ogit:onAttribute',
            'ogit:onVertex',
            'ogit:operation',
            'ogit:priority',
            'ogit:severity',
            'ogit:sourceId',
            'ogit:type'},
        allowed_connections={
            ('ogit:hiddenBy', 'ogit:Person'),
            ('ogit:readBy', 'ogit:Person'),
            ('ogit:seenBy', 'ogit:Person'),
            ('ogit:triggers', 'ogit:Event')})
    yield Entity(
        about='ogit.OSLC-arch:LinkType',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-arch:Resource',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-asset:Artifact',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-asset:Asset',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-automation:AutomationPlan',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-automation:AutomationRequest',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-automation:AutomationResult',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-automation:ParameterInstance',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-automation:TeardownAction',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-change:ChangeRequest',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:AllowedValues',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Comment',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Compact',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:CreationFactory',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Dialog',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Discussion',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Error',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:ExtendedError',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:OAuthConfiguration',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:PrefixDefinition',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Preview',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Property',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Publisher',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:QueryCapability',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:ResourceShape',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:ResponseInfo',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:Service',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:ServiceProvider',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-core:ServiceProviderCatalog',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:ComputerSystem',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:Database',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:IPAddress',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:OperatingSystem',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:Path',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:Process',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:ServerAccessPoint',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:ServiceInstance',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.OSLC-crtv:runsOn', 'ogit.Automation:MARSNode'),
            ('ogit.OSLC-crtv:runsOn', 'ogit.MARS:Machine'),
            ('ogit:uses', 'ogit.Automation:KnowledgePool')})
    yield Entity(
        about='ogit.OSLC-crtv:SoftwareModule',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:SoftwareServer',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:StorageVolume',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-crtv:Tablespace',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Baseline',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:BaselineList',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:memberBaseline', 'ogit.OSLC-ems:Baseline')})
    yield Entity(
        about='ogit.OSLC-ems:CdfPoint',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:CumulativeDistributionFunction',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:cdfPoint', 'ogit.OSLC-ems:CdfPoint')})
    yield Entity(
        about='ogit.OSLC-ems:Dimension',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:DimensionCell',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:DimensionColumn',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:DimensionMember',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:EffortMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Estimate',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.OSLC-ems:predicts', 'ogit.OSLC-ems:MeasureDistribution'),
            ('ogit.OSLC-ems:predictsTable', 'ogit.OSLC-ems:FactDistributionTable'),
            ('ogit.OSLC-ems:predictsWbs', 'ogit.OSLC-ems:WorkBreakdownStructure')})
    yield Entity(
        about='ogit.OSLC-ems:EstimateList',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Fact',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:FactDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:FactDistributionTable',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:FactTable',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:FinancialMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Format',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Grain',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Head',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Map',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:mapping', 'ogit.OSLC-ems:Mapping')})
    yield Entity(
        about='ogit.OSLC-ems:Mapping',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:to', 'ogit.OSLC-ems:DimensionMember')})
    yield Entity(
        about='ogit.OSLC-ems:Measure',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:unitOfMeasure', 'ogit.OSLC-ems:UnitOfMeasure')})
    yield Entity(
        about='ogit.OSLC-ems:MeasureCell',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:MeasureColumn',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:MeasureDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:MeasureDistributionCell',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Measurement',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:MeasurementList',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:memberMeasurement', 'ogit.OSLC-ems:Measurement')})
    yield Entity(
        about='ogit.OSLC-ems:Metric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:NormalDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:PointEstimate',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:PoissonDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:ProbabilityDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:ProcessMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:ProductivityMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Project',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:currentBaseline', 'ogit.OSLC-ems:Baseline')})
    yield Entity(
        about='ogit.OSLC-ems:ProjectList',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:memberProject', 'ogit.OSLC-ems:Project')})
    yield Entity(
        about='ogit.OSLC-ems:Quantile',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:QuantileFunction',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:quantile', 'ogit.OSLC-ems:Quantile')})
    yield Entity(
        about='ogit.OSLC-ems:ReliabilityMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:Scenario',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.OSLC-ems:assumes', 'ogit.OSLC-ems:MeasureDistribution'),
            ('ogit.OSLC-ems:assumesTable', 'ogit.OSLC-ems:FactDistributionTable'),
            ('ogit.OSLC-ems:assumesWbs', 'ogit.OSLC-ems:WorkBreakdownStructure'),
            ('ogit.OSLC-ems:extendsScenario', 'ogit.OSLC-ems:Scenario')})
    yield Entity(
        about='ogit.OSLC-ems:ScenarioList',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:memberScenario', 'ogit.OSLC-ems:Scenario')})
    yield Entity(
        about='ogit.OSLC-ems:Service',
        parent='ogit:Node',
        allowed_connections={
            ('ogit.OSLC-ems:baselineList', 'ogit.OSLC-ems:BaselineList'),
            ('ogit.OSLC-ems:estimateList', 'ogit.OSLC-ems:EstimateList'),
            ('ogit.OSLC-ems:measurementList', 'ogit.OSLC-ems:MeasurementList'),
            ('ogit.OSLC-ems:projectList', 'ogit.OSLC-ems:ProjectList'),
            ('ogit.OSLC-ems:scenarioList', 'ogit.OSLC-ems:ScenarioList')})
    yield Entity(
        about='ogit.OSLC-ems:SizeMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:TimeMetric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:TriangularDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:UniformDistribution',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:UnitOfMeasure',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:WbsFormat',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-ems:WorkBreakdownStructure',
        parent='ogit:Node',
        allowed_connections={('ogit.OSLC-ems:wbsFormat', 'ogit.OSLC-ems:WbsFormat')})
    yield Entity(
        about='ogit.OSLC-perfmon:AvgJmsGetTime',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:AvgLoginRequestFailures',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:AvgRequestFailures',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:BufferPoolHits',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:BufferPoolMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:CpuMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:CpuSpeed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:CpuUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:DiskMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:DiskSpaceOverCommitAmount',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:DiskSpaceUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:FailureMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:GarbageCollectionRequests',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:HeapMemoryUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:HighDepthQueueCount',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:HostedDatabases',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:LocalInboundConnections',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:LockListUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:LogUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:LoginRequestFailures',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:MemoryAvailableAfterGarbageCollection',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:MemoryMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:MessageCount',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:Metric',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:NetworkIOErrors',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:NetworkMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:PerMinute',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:PerformanceMonitoringRecord',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:QueueDepth',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:QueueFull',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:RealMemoryUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:RemoteInboundConnections',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:RequestFailures',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:RequestMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceAvailabilityMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceExhaustionMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ResourceUsageMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ResponseTime',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ResponseTimeMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:SortOverflows',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:SqlStatmentFailures',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:TableSpaceFree',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:TableSpaceUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:ThreadPoolMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:TimeDatabaseThreadPoolExhausted',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:TimeJCAThreadPoolExhausted',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:TimeThreadPoolExhausted',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:VirtualMemoryUsed',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:VirtualizationMetrics',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-perfmon:VmCpuReady',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-qm:TestCase',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-qm:TestExecutionRecord',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-qm:TestPlan',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-qm:TestResult',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-qm:TestScript',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-reqman:Requirement',
        parent='ogit:Node')
    yield Entity(
        about='ogit.OSLC-reqman:RequirementCollection',
        parent='ogit:Node')
    yield Entity(
        about='ogit:OntologyAttribute',
        parent='ogit:Node',
        required_attributes={
            'ogit:ontologyAdminContact',
            'ogit:ontologyCreated',
            'ogit:ontologyCreator',
            'ogit:ontologyDescription',
            'ogit:ontologyId',
            'ogit:ontologyModified',
            'ogit:ontologyName',
            'ogit:ontologyTechContact',
            'ogit:ontologyValidFrom'},
        optional_attributes={
            'ogit:ontologyDeleter',
            'ogit:ontologyHide',
            'ogit:ontologyValidationParameter',
            'ogit:ontologyValidationType'})
    yield Entity(
        about='ogit:OntologyEntity',
        parent='ogit:Node',
        required_attributes={
            'ogit:description',
            'ogit:ontologyAdminContact',
            'ogit:ontologyCreated',
            'ogit:ontologyCreator',
            'ogit:ontologyDescription',
            'ogit:ontologyId',
            'ogit:ontologyModified',
            'ogit:ontologyName',
            'ogit:ontologyParent',
            'ogit:ontologyScope',
            'ogit:ontologyTechContact',
            'ogit:ontologyValidFrom'},
        optional_attributes={
            'ogit:ontologyDeleter',
            'ogit:ontologyHide',
            'ogit:ontologyValidUntil'},
        allowed_connections={
            ('ogit:demands', 'ogit:OntologyAttribute'),
            ('ogit:index', 'ogit:OntologyAttribute'),
            ('ogit:opts', 'ogit:OntologyAttribute'),
            ('ogit:uses', 'ogit:Schema')})
    yield Entity(
        about='ogit:OntologyVerb',
        parent='ogit:Node',
        required_attributes={
            'ogit:ontologyAdminContact',
            'ogit:ontologyCreated',
            'ogit:ontologyCreator',
            'ogit:ontologyDescription',
            'ogit:ontologyId',
            'ogit:ontologyModified',
            'ogit:ontologyName',
            'ogit:ontologyTechContact',
            'ogit:ontologyValidFrom'},
        optional_attributes={
            'ogit:ontologyCardinality',
            'ogit:ontologyDeleter',
            'ogit:ontologyHide'})
    yield Entity(
        about='ogit:Organization',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:businessCategory',
            'ogit:city',
            'ogit:country',
            'ogit:description',
            'ogit:email',
            'ogit:function',
            'ogit:phone',
            'ogit:postalCode',
            'ogit:sourceId',
            'ogit:status',
            'ogit:streetAddress',
            'ogit:webPage'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit.MRO.Aviation:orders', 'ogit.MRO.Aviation:Layover'),
            ('ogit:approves', 'ogit:ConfigurationItem'),
            ('ogit:approves', 'ogit:ConfigurationItem'),
            ('ogit:associates', 'ogit:Role'),
            ('ogit:belongs', 'ogit:Alert'),
            ('ogit:communicatesWith', 'ogit:Organization'),
            ('ogit:competes', 'ogit:Organization'),
            ('ogit:complies', 'ogit:Policy'),
            ('ogit:concludes', 'ogit:Contract'),
            ('ogit:consumes', 'ogit.Project:Project'),
            ('ogit:consumes', 'ogit.Survey:Iteration'),
            ('ogit:contains', 'ogit:Organization'),
            ('ogit:creates', 'ogit:Certificate'),
            ('ogit:creates', 'ogit:ConfigurationItem'),
            ('ogit:creates', 'ogit:Organization'),
            ('ogit:defines', 'ogit:Role'),
            ('ogit:defines', 'ogit.ServiceManagement:Offering'),
            ('ogit:deliversTo', 'ogit:Organization'),
            ('ogit:employs', 'ogit:Person'),
            ('ogit:generates', 'ogit:Catalog'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:governs', 'ogit:Organization'),
            ('ogit:hosts', 'ogit:Environment'),
            ('ogit:leads', 'ogit:Organization'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:manages', 'ogit:ConfigurationItem'),
            ('ogit:manages', 'ogit.Datacenter:Building'),
            ('ogit:manages', 'ogit.Datacenter:Cooling'),
            ('ogit:manages', 'ogit.Datacenter:Datacenter'),
            ('ogit:manages', 'ogit.Datacenter:Rack'),
            ('ogit:manages', 'ogit.Datacenter:Room'),
            ('ogit:manages', 'ogit:Device'),
            ('ogit:manages', 'ogit.Health.Diagnostics:Equipment'),
            ('ogit:manages', 'ogit:Organization'),
            ('ogit:manages', 'ogit.Software:Application'),
            ('ogit:organizes', 'ogit.Schedule:Event'),
            ('ogit:owns', 'ogit:Asset'),
            ('ogit:owns', 'ogit.Automation:MARSNode'),
            ('ogit:owns', 'ogit:Certificate'),
            ('ogit:owns', 'ogit.MRO.Aviation:Aircraft'),
            ('ogit:plans', 'ogit.Cost:Budget'),
            ('ogit:produces', 'ogit:Product'),
            ('ogit:produces', 'ogit.Project:Project'),
            ('ogit:produces', 'ogit.Survey:Iteration'),
            ('ogit:provides', 'ogit:ConfigurationItem'),
            ('ogit:relates', 'ogit:Organization'),
            ('ogit:represents', 'ogit:Organization'),
            ('ogit:represents', 'ogit:Person'),
            ('ogit:sellsTo', 'ogit:Organization'),
            ('ogit:supervises', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:supervises', 'ogit.ServiceManagement:Incident'),
            ('ogit:supervises', 'ogit.ServiceManagement:Order'),
            ('ogit:supervises', 'ogit.ServiceManagement:Problem'),
            ('ogit:supervises', 'ogit.ServiceManagement:SubTask'),
            ('ogit:supervises', 'ogit.ServiceManagement:Ticket'),
            ('ogit:supports', 'ogit:ConfigurationItem'),
            ('ogit:supports', 'ogit:Organization'),
            ('ogit:supports', 'ogit.Project:Project'),
            ('ogit:supports', 'ogit.Survey:Iteration'),
            ('ogit:uses', 'ogit:License'),
            ('ogit:uses', 'ogit:Product')})
    yield Entity(
        about='ogit.PTF:Dummy',
        parent='ogit:Node',
        indexed_attributes={'ogit:name'},
        allowed_connections={('ogit:relates', 'ogit.PTF:Dummy')})
    yield Entity(
        about='ogit.PTF:HiroTopology',
        parent='ogit:Node',
        optional_attributes={
            'ogit.PTF:dbAwsMachineCnt',
            'ogit.PTF:dbAwsMachineType',
            'ogit.PTF:engineAwsMachineCnt',
            'ogit.PTF:engineAwsMachineType',
            'ogit.PTF:graphAwsMachineCnt',
            'ogit.PTF:graphAwsMachineType',
            'ogit.PTF:hiroVsn',
            'ogit.PTF:iamAwsMachineCnt',
            'ogit.PTF:iamAwsMachineType',
            'ogit.PTF:revProxyAwsMachineCnt',
            'ogit.PTF:revProxyAwsMachineType'},
        indexed_attributes={'ogit:name'},
        allowed_connections={('ogit:relates', 'ogit.PTF:Test')})
    yield Entity(
        about='ogit.PTF:Test',
        parent='ogit:Node',
        required_attributes={
            'ogit.PTF:startTime',
            'ogit:name'},
        optional_attributes={
            'ogit.PTF:callCnt',
            'ogit.PTF:clientCnt',
            'ogit.PTF:duration',
            'ogit.PTF:endTime',
            'ogit.PTF:graphNodesCnt',
            'ogit.PTF:hotTest',
            'ogit.PTF:issuesCnt',
            'ogit.PTF:kisCnt',
            'ogit.PTF:linksCnt',
            'ogit.PTF:vertexSearchCount',
            'ogit.PTF:vertexSearchFull'},
        allowed_connections={('ogit:relates', 'ogit.PTF:HiroTopology')})
    yield Entity(
        about='ogit:Parameter',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.ServiceManagement:granularity',
            'ogit.ServiceManagement:isRequired',
            'ogit.ServiceManagement:requirementId',
            'ogit:category',
            'ogit:description',
            'ogit:isMutable',
            'ogit:lengthOfReportingPeriod',
            'ogit:unit',
            'ogit:uri',
            'ogit:values'},
        allowed_connections={
            ('ogit:describes', 'ogit:CatalogItem'),
            ('ogit:describes', 'ogit.Cost:CostElement'),
            ('ogit:describes', 'ogit.ServiceManagement:Offering'),
            ('ogit:describes', 'ogit.ServiceManagement:SLA'),
            ('ogit:describes', 'ogit.ServiceManagement:Service'),
            ('ogit:proves', 'ogit:Parameter'),
            ('ogit:reports', 'ogit:Parameter'),
            ('ogit:specifies', 'ogit.Price:PriceSpecification')})
    yield Entity(
        about='ogit:ParameterType',
        parent='ogit:Node',
        required_attributes={
            'ogit:enumValues',
            'ogit:name'},
        allowed_connections={('ogit:corresponds', 'ogit:Parameter')})
    yield Entity(
        about='ogit:Penalty',
        parent='ogit:Node',
        optional_attributes={'ogit:description'})
    yield Entity(
        about='ogit:Person',
        parent='ogit:Node',
        optional_attributes={
            'ogit:alternativeName',
            'ogit:email',
            'ogit:fax',
            'ogit:firstName',
            'ogit:lastName',
            'ogit:middleName',
            'ogit:mobilePhone',
            'ogit:notification',
            'ogit:officePhone',
            'ogit:otherPhone',
            'ogit:position',
            'ogit:sourceId',
            'ogit:status',
            'ogit:title',
            'ogit:webPage'},
        indexed_attributes={
            'ogit:alternativeName',
            'ogit:email',
            'ogit:firstName',
            'ogit:lastName'},
        allowed_connections={
            ('ogit.UserMeta:loses', 'ogit.UserMeta:Game'),
            ('ogit.UserMeta:plays', 'ogit.UserMeta:Game'),
            ('ogit.UserMeta:wins', 'ogit.UserMeta:Game'),
            ('ogit:accepts', 'ogit:TermsAndConditions'),
            ('ogit:approves', 'ogit:Contract'),
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:closes', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:closes', 'ogit.ServiceManagement:Incident'),
            ('ogit:closes', 'ogit.ServiceManagement:Order'),
            ('ogit:closes', 'ogit.ServiceManagement:Problem'),
            ('ogit:closes', 'ogit.ServiceManagement:SubTask'),
            ('ogit:closes', 'ogit.ServiceManagement:Ticket'),
            ('ogit:communicatesWith', 'ogit:Person'),
            ('ogit:complies', 'ogit:Role'),
            ('ogit:concludes', 'ogit:Contract'),
            ('ogit:consumes', 'ogit.Project:Milestone'),
            ('ogit:consumes', 'ogit.Project:Project'),
            ('ogit:creates', 'ogit:Alert'),
            ('ogit:creates', 'ogit:Certificate'),
            ('ogit:creates', 'ogit:ConfigurationItem'),
            ('ogit:creates', 'ogit.SalesDistribution:SalesOrder'),
            ('ogit:defines', 'ogit.UserMeta:Filter'),
            ('ogit:dislikes', 'ogit:Person'),
            ('ogit:follows', 'ogit:Person'),
            ('ogit:has', 'ogit.Mobile:HealthInfo'),
            ('ogit:ignores', 'ogit:Comment'),
            ('ogit:installs', 'ogit.Software:Application'),
            ('ogit:invites', 'ogit:Person'),
            ('ogit:leads', 'ogit:Organization'),
            ('ogit:likes', 'ogit:Person'),
            ('ogit:likes', 'ogit.UserMeta:Preferences'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:manages', 'ogit.Datacenter:Building'),
            ('ogit:manages', 'ogit.Datacenter:Cooling'),
            ('ogit:manages', 'ogit.Datacenter:Datacenter'),
            ('ogit:manages', 'ogit.Datacenter:Rack'),
            ('ogit:manages', 'ogit.Datacenter:Room'),
            ('ogit:manages', 'ogit:Device'),
            ('ogit:manages', 'ogit.Health.Diagnostics:Equipment'),
            ('ogit:manages', 'ogit.Health.Diagnostics:Test'),
            ('ogit:manages', 'ogit.Network:Port'),
            ('ogit:manages', 'ogit.Network:PortChannel'),
            ('ogit:manages', 'ogit.Network:Router'),
            ('ogit:manages', 'ogit.Network:Shelf'),
            ('ogit:manages', 'ogit.Network:Slot'),
            ('ogit:manages', 'ogit.Network:Subnet'),
            ('ogit:manages', 'ogit.Network:Switch'),
            ('ogit:manages', 'ogit.Network:VLAN'),
            ('ogit:manages', 'ogit.Network:WifiAccessPoint'),
            ('ogit:manages', 'ogit:Organization'),
            ('ogit:manages', 'ogit.Project:Project'),
            ('ogit:manages', 'ogit.Software:Application'),
            ('ogit:opens', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:opens', 'ogit.ServiceManagement:Incident'),
            ('ogit:opens', 'ogit.ServiceManagement:Order'),
            ('ogit:opens', 'ogit.ServiceManagement:Problem'),
            ('ogit:opens', 'ogit.ServiceManagement:SubTask'),
            ('ogit:opens', 'ogit.ServiceManagement:Ticket'),
            ('ogit:owns', 'ogit:Certificate'),
            ('ogit:owns', 'ogit:Event'),
            ('ogit:owns', 'ogit.ServiceManagement:Service'),
            ('ogit:owns', 'ogit.Software:Application'),
            ('ogit:owns', 'ogit:Vcard'),
            ('ogit:produces', 'ogit.Project:Milestone'),
            ('ogit:produces', 'ogit.Project:Project'),
            ('ogit:receives', 'ogit:Notification'),
            ('ogit:registeredAt', 'ogit.Location:Address'),
            ('ogit:rejects', 'ogit:Alert'),
            ('ogit:relates', 'ogit.Survey:Iteration'),
            ('ogit:repliedWith', 'ogit.Survey:Reply'),
            ('ogit:reports', 'ogit:Person'),
            ('ogit:reports', 'ogit.ServiceManagement:Incident'),
            ('ogit:reports', 'ogit.ServiceManagement:Problem'),
            ('ogit:represents', 'ogit:Organization'),
            ('ogit:represents', 'ogit:Person'),
            ('ogit:requests', 'ogit:LicenseRequest'),
            ('ogit:requests', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:requests', 'ogit.ServiceManagement:SubTask'),
            ('ogit:sends', 'ogit:Notification'),
            ('ogit:supervises', 'ogit:Contract'),
            ('ogit:supervises', 'ogit.Project:Project'),
            ('ogit:supervises', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:supervises', 'ogit.ServiceManagement:Incident'),
            ('ogit:supervises', 'ogit.ServiceManagement:Order'),
            ('ogit:supervises', 'ogit.ServiceManagement:Problem'),
            ('ogit:supervises', 'ogit.ServiceManagement:SubTask'),
            ('ogit:supervises', 'ogit.ServiceManagement:Ticket'),
            ('ogit:supports', 'ogit:ConfigurationItem'),
            ('ogit:supports', 'ogit.Project:Milestone'),
            ('ogit:supports', 'ogit.Project:Project'),
            ('ogit:tracks', 'ogit:Timeseries'),
            ('ogit:updates', 'ogit:ConfigurationItem'),
            ('ogit:updates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:updates', 'ogit.ServiceManagement:Incident'),
            ('ogit:updates', 'ogit.ServiceManagement:Order'),
            ('ogit:updates', 'ogit.ServiceManagement:Problem'),
            ('ogit:updates', 'ogit.ServiceManagement:SubTask'),
            ('ogit:updates', 'ogit.ServiceManagement:Ticket'),
            ('ogit:uses', 'ogit.Cost:Budget'),
            ('ogit:uses', 'ogit.Health.Diagnostics:TestStation'),
            ('ogit:uses', 'ogit:License'),
            ('ogit:uses', 'ogit.Mobile:AppInstance'),
            ('ogit:uses', 'ogit.Mobile:LicenceCodes'),
            ('ogit:uses', 'ogit.OSLC-crtv:ServiceInstance'),
            ('ogit:uses', 'ogit.Software:Application'),
            ('ogit:worksOn', 'ogit:Status')})
    yield Entity(
        about='ogit:Policy',
        parent='ogit:Node',
        required_attributes={'ogit:content'},
        allowed_connections={('ogit:governs', 'ogit.ServiceManagement:Service')})
    yield Entity(
        about='ogit.Price:Invoice',
        parent='ogit:Node',
        required_attributes={
            'ogit.Price:priceAmount',
            'ogit:currency'},
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:bills', 'ogit.ServiceManagement:Order')})
    yield Entity(
        about='ogit.Price:PriceSpecification',
        parent='ogit:Node')
    yield Entity(
        about='ogit.Procurement:ProductionOrder',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Procurement:productionOrderId',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.Procurement:PurchaseOrder',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Procurement:purchaseOrderId',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit.Procurement:PurchaseOrderItem')})
    yield Entity(
        about='ogit.Procurement:PurchaseOrderItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit:Product',
        parent='ogit:Node',
        optional_attributes={'ogit:name'})
    yield Entity(
        about='ogit.Project:Milestone',
        parent='ogit:Node',
        optional_attributes={
            'ogit:category',
            'ogit:finishedAt',
            'ogit:plannedFinishDate',
            'ogit:plannedStartDate',
            'ogit:startedAt',
            'ogit:status',
            'ogit:title'},
        indexed_attributes={'ogit:title'},
        allowed_connections={('ogit:belongs', 'ogit.Project:Project')})
    yield Entity(
        about='ogit.Project:Project',
        parent='ogit:Node',
        optional_attributes={
            'ogit:category',
            'ogit:finishedAt',
            'ogit:placement',
            'ogit:plannedFinishDate',
            'ogit:plannedStartDate',
            'ogit:startedAt',
            'ogit:status',
            'ogit:title'},
        indexed_attributes={'ogit:title'})
    yield Entity(
        about='ogit:Question',
        parent='ogit:Node',
        optional_attributes={
            'ogit:capacity',
            'ogit:question',
            'ogit:response',
            'ogit:status'},
        allowed_connections={('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.RDDL:Namespace',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RDDL:Resource',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RPA:Controller',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RPA:Object',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RPA:Robot',
        parent='ogit:Node',
        optional_attributes={
            'ogit:BatteryState',
            'ogit.RPA:Odometry'},
        allowed_connections={
            ('ogit.RPA:Operates', 'ogit.RPA:RoboticEnvironment'),
            ('ogit:belongs', 'ogit.RPA:Object'),
            ('ogit:consistsOf', 'ogit.RPA:Controller'),
            ('ogit:consistsOf', 'ogit.RPA:Sensor'),
            ('ogit:isPartOf', 'ogit.RPA:RoboticSystem')})
    yield Entity(
        about='ogit.RPA:RoboticEnvironment',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RPA:RoboticSystem',
        parent='ogit:Node')
    yield Entity(
        about='ogit.RPA:Sensor',
        parent='ogit:Node')
    yield Entity(
        about='ogit:Rating',
        parent='ogit:Node',
        required_attributes={'ogit:value'},
        optional_attributes={'ogit:comment'},
        allowed_connections={('ogit:rates', 'ogit.Auth:Application')})
    yield Entity(
        about='ogit:Region',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit:Relevance',
        parent='ogit:Node',
        optional_attributes={'ogit:occurenceCount'})
    yield Entity(
        about='ogit:Role',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:status'},
        allowed_connections={
            ('ogit:desires', 'ogit.HR.Recruiting:Education'),
            ('ogit:manages', 'ogit.ServiceManagement:Service'),
            ('ogit:reports', 'ogit:Role'),
            ('ogit:requires', 'ogit.HR.Recruiting:Education'),
            ('ogit:uses', 'ogit.HR.Recruiting:Relevance')})
    yield Entity(
        about='ogit.SaaS:Component',
        required_attributes={
            'ogit.Version:major',
            'ogit.Version:minor',
            'ogit.Version:patch',
            'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:status'},
        indexed_attributes={'ogit:name'})
    yield Entity(
        about='ogit.SaaS:ComponentInstance',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:sourceId',
            'ogit:status'},
        indexed_attributes={'ogit:id'},
        allowed_connections={('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.SaaS:ConfigurationTemplate',
        required_attributes={'ogit:id'},
        optional_attributes={'ogit:description'},
        indexed_attributes={'ogit:id'},
        allowed_connections={('ogit:configures', 'ogit.SaaS:Component')})
    yield Entity(
        about='ogit.SaaS:Deployment',
        required_attributes={
            'ogit:id',
            'ogit:status'},
        optional_attributes={
            'ogit:comment',
            'ogit:sourceId',
            'ogit:status'},
        indexed_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:contains', 'ogit.SaaS:ComponentInstance'),
            ('ogit:contains', 'ogit.SaaS:Deployment')})
    yield Entity(
        about='ogit.SaaS:DeploymentTemplate',
        required_attributes={
            'ogit.Version:major',
            'ogit.Version:minor',
            'ogit.Version:patch',
            'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:status'},
        indexed_attributes={'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit.SaaS:ConfigurationTemplate')})
    yield Entity(
        about='ogit.SalesDistribution:Customer',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.SalesDistribution:customerId',
            'ogit:description'},
        allowed_connections={
            ('ogit:belongs', 'ogit.MARS:Application'),
            ('ogit:creates', 'ogit.SalesDistribution:SalesOrder'),
            ('ogit:has', 'ogit.SalesDistribution:OpenItem'),
            ('ogit:provides', 'ogit.SalesDistribution:Payment'),
            ('ogit:receives', 'ogit.SalesDistribution:Delivery'),
            ('ogit:receives', 'ogit.SalesDistribution:Invoice')})
    yield Entity(
        about='ogit.SalesDistribution:Delivery',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:deliveryId',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:assignedTo', 'ogit.SalesDistribution:Shipment'),
            ('ogit:contains', 'ogit.SalesDistribution:DeliveryItem')})
    yield Entity(
        about='ogit.SalesDistribution:DeliveryItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={
            ('ogit:corresponds', 'ogit.SalesDistribution:InvoiceItem'),
            ('ogit:corresponds', 'ogit.SalesDistribution:ShipmentItem')})
    yield Entity(
        about='ogit.SalesDistribution:Equipment',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.SalesDistribution:Invoice',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:invoiceDate',
            'ogit.SalesDistribution:invoiceId',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit.SalesDistribution:invoiceDate',
            'ogit.SalesDistribution:invoiceId',
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit.SalesDistribution:InvoiceItem')})
    yield Entity(
        about='ogit.SalesDistribution:InvoiceItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:amount',
            'ogit:currency',
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:corresponds', 'ogit.SalesDistribution:OpenItem')})
    yield Entity(
        about='ogit.SalesDistribution:OpenItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:amount',
            'ogit:currency',
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:belongs', 'ogit.SalesDistribution:Payment')})
    yield Entity(
        about='ogit.SalesDistribution:Payment',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:amount',
            'ogit.SalesDistribution:transactionDate',
            'ogit.SalesDistribution:transactionId',
            'ogit.SalesDistribution:valueDate',
            'ogit:currency',
            'ogit:description',
            'ogit:name',
            'ogit:status'},
        allowed_connections={('ogit:belongs', 'ogit.SalesDistribution:SalesOrder')})
    yield Entity(
        about='ogit.SalesDistribution:SalesOrder',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:amount',
            'ogit.SalesDistribution:orderDate',
            'ogit.SalesDistribution:salesOrderId',
            'ogit:currency',
            'ogit:description',
            'ogit:name',
            'ogit:status'},
        allowed_connections={
            ('ogit:belongs', 'ogit.MARS:Application'),
            ('ogit:causes', 'ogit.SalesDistribution:Delivery'),
            ('ogit:causes', 'ogit.SalesDistribution:Invoice'),
            ('ogit:contains', 'ogit.SalesDistribution:SalesOrderItem'),
            ('ogit:triggers', 'ogit.Procurement:ProductionOrder'),
            ('ogit:triggers', 'ogit.Procurement:PurchaseOrder')})
    yield Entity(
        about='ogit.SalesDistribution:SalesOrderItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:corresponds', 'ogit.SalesDistribution:DeliveryItem')})
    yield Entity(
        about='ogit.SalesDistribution:Shipment',
        parent='ogit:Node',
        optional_attributes={
            'ogit.SalesDistribution:shipmentId',
            'ogit:description',
            'ogit:name'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'},
        allowed_connections={('ogit:contains', 'ogit.SalesDistribution:ShipmentItem')})
    yield Entity(
        about='ogit.SalesDistribution:ShipmentItem',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit.Schedule:Activity',
        parent='ogit:Node',
        optional_attributes={
            'ogit.Schedule:dependencies',
            'ogit.Schedule:resources',
            'ogit:description',
            'ogit:rank',
            'ogit:status',
            'ogit:subType',
            'ogit:title'},
        allowed_connections={('ogit:dependsOn', 'ogit.Schedule:Activity')})
    yield Entity(
        about='ogit.Schedule:Attendee',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.Schedule:attendanceStatus',
            'ogit.Schedule:isOrganizer',
            'ogit:email'},
        allowed_connections={('ogit:has', 'ogit.Auth:Account')})
    yield Entity(
        about='ogit.Schedule:Calendar',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:subType',
            'ogit:title'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Auth:Account'),
            ('ogit:contains', 'ogit.Schedule:Event')})
    yield Entity(
        about='ogit.Schedule:Event',
        parent='ogit:Node',
        required_attributes={
            'ogit.Schedule:endTime',
            'ogit.Schedule:startTime'},
        optional_attributes={
            'ogit.Schedule:location',
            'ogit:description',
            'ogit:subType',
            'ogit:title'},
        allowed_connections={
            ('ogit:has', 'ogit.Schedule:Attendee'),
            ('ogit:locatedAt', 'ogit.Location:Address')})
    yield Entity(
        about='ogit.Schedule:Schedule',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:title'},
        allowed_connections={('ogit:contains', 'ogit.Schedule:Activity')})
    yield Entity(
        about='ogit:Schema',
        parent='ogit:Node',
        required_attributes={'ogit:content'},
        optional_attributes={
            'ogit:name',
            'ogit:uri'})
    yield Entity(
        about='ogit:Series',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:name'},
        optional_attributes={
            'ogit:creator',
            'ogit:description'},
        allowed_connections={('ogit:contains', 'ogit:Course')})
    yield Entity(
        about='ogit.ServiceManagement:Action',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:id'},
        allowed_connections={
            ('ogit:corresponds', 'ogit:CatalogItem'),
            ('ogit:requires', 'ogit:CatalogItem'),
            ('ogit:requires', 'ogit.ServiceManagement:Action'),
            ('ogit:requires', 'ogit.ServiceManagement:Service')})
    yield Entity(
        about='ogit.ServiceManagement:ApprovalTask',
        parent='ogit:Node',
        optional_attributes={
            'ogit.ServiceManagement:approvalStatus',
            'ogit.ServiceManagement:sourceStatus',
            'ogit:id',
            'ogit:lastUpdatedAt',
            'ogit:name',
            'ogit:reason'},
        allowed_connections={
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:belongs', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:corresponds', 'ogit:Task'),
            ('ogit:precedes', 'ogit.ServiceManagement:ApprovalTask')})
    yield Entity(
        about='ogit.ServiceManagement:ChangeRequest',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:changeStatus',
            'ogit.ServiceManagement:customer',
            'ogit.ServiceManagement:fallbackPlan',
            'ogit.ServiceManagement:implementationPlan',
            'ogit.ServiceManagement:resolutionCode',
            'ogit.ServiceManagement:scheduledFinishAt',
            'ogit.ServiceManagement:scheduledStartAt',
            'ogit.ServiceManagement:solution',
            'ogit.ServiceManagement:sourceStatus',
            'ogit.ServiceManagement:targetFinishAt',
            'ogit.ServiceManagement:targetStartAt',
            'ogit.ServiceManagement:testPlan',
            'ogit:assignedGroup',
            'ogit:category',
            'ogit:effort',
            'ogit:finishedAt',
            'ogit:justification',
            'ogit:reportedAt',
            'ogit:reviewedAt',
            'ogit:risk',
            'ogit:startedAt'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit:ConfigurationItem'),
            ('ogit:affects', 'ogit:Location'),
            ('ogit:affects', 'ogit.MARS:Application'),
            ('ogit:affects', 'ogit.MARS:Machine'),
            ('ogit:affects', 'ogit.MARS:Resource'),
            ('ogit:affects', 'ogit.MARS:Software'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:affects', 'ogit.ServiceManagement:Service'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit.ServiceManagement:Service'),
            ('ogit:causes', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:causes', 'ogit.ServiceManagement:Order'),
            ('ogit:complies', 'ogit.ServiceManagement:SLA'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:corresponds', 'ogit.ServiceManagement:Ticket'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.MARS:Application'),
            ('ogit:relates', 'ogit.MARS:Machine'),
            ('ogit:relates', 'ogit.MARS:Resource'),
            ('ogit:relates', 'ogit.MARS:Software'),
            ('ogit:relates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:relates', 'ogit.ServiceManagement:Incident'),
            ('ogit:relates', 'ogit.ServiceManagement:Order'),
            ('ogit:relates', 'ogit.ServiceManagement:Problem'),
            ('ogit:reportedOn', 'ogit.Automation:MARSNode'),
            ('ogit:reportedOn', 'ogit.MARS:Application'),
            ('ogit:reportedOn', 'ogit.MARS:Machine'),
            ('ogit:reportedOn', 'ogit.MARS:Resource'),
            ('ogit:reportedOn', 'ogit.MARS:Software'),
            ('ogit:uses', 'ogit.ServiceManagement:ChangeRequest')})
    yield Entity(
        about='ogit.ServiceManagement:Incident',
        parent='ogit:Node',
        optional_attributes={
            'ogit.ServiceManagement:customer',
            'ogit.ServiceManagement:incidentStatus',
            'ogit.ServiceManagement:reportedSource',
            'ogit.ServiceManagement:resolutionCode',
            'ogit.ServiceManagement:resolvedAt',
            'ogit.ServiceManagement:solution',
            'ogit.ServiceManagement:sourceStatus',
            'ogit.ServiceManagement:task',
            'ogit:assignedGroup',
            'ogit:category',
            'ogit:id',
            'ogit:reportedAt'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit:ConfigurationItem'),
            ('ogit:affects', 'ogit.MARS:Application'),
            ('ogit:affects', 'ogit.MARS:Machine'),
            ('ogit:affects', 'ogit.MARS:Resource'),
            ('ogit:affects', 'ogit.MARS:Software'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:affects', 'ogit.ServiceManagement:Service'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit.ServiceManagement:Service'),
            ('ogit:causes', 'ogit:Event'),
            ('ogit:causes', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:causes', 'ogit.ServiceManagement:Incident'),
            ('ogit:causes', 'ogit.ServiceManagement:Order'),
            ('ogit:causes', 'ogit.ServiceManagement:Problem'),
            ('ogit:complies', 'ogit.ServiceManagement:SLA'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:corresponds', 'ogit.ServiceManagement:Ticket'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:opens', 'ogit:Task'),
            ('ogit:relates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:relates', 'ogit.ServiceManagement:Incident'),
            ('ogit:relates', 'ogit.ServiceManagement:Problem'),
            ('ogit:reportedOn', 'ogit.Automation:MARSNode'),
            ('ogit:reportedOn', 'ogit.MARS:Application'),
            ('ogit:reportedOn', 'ogit.MARS:Machine'),
            ('ogit:reportedOn', 'ogit.MARS:Resource'),
            ('ogit:reportedOn', 'ogit.MARS:Software')})
    yield Entity(
        about='ogit.ServiceManagement:Offering',
        parent='ogit:Node',
        required_attributes={
            'ogit:id',
            'ogit:name'},
        optional_attributes={
            'ogit.ServiceManagement:allowedForNewBusiness',
            'ogit:capacityAvailable',
            'ogit:category',
            'ogit:currency',
            'ogit:description',
            'ogit:expirationDate',
            'ogit:market',
            'ogit:serialNumber',
            'ogit:validFrom'},
        allowed_connections={
            ('ogit:availableIn', 'ogit:Region'),
            ('ogit:contains', 'ogit:CatalogItem'),
            ('ogit:contains', 'ogit.Cost:CostElement'),
            ('ogit:contains', 'ogit.ServiceManagement:Order'),
            ('ogit:contains', 'ogit.ServiceManagement:Service'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:specifies', 'ogit.Automation:MARSModelTemplate')})
    yield Entity(
        about='ogit.ServiceManagement:Order',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:externalTicketId',
            'ogit.ServiceManagement:externalTicketSource',
            'ogit.ServiceManagement:reportedSource',
            'ogit.ServiceManagement:sourceStatus',
            'ogit:closedAt',
            'ogit:createdAt',
            'ogit:description',
            'ogit:impact',
            'ogit:lastUpdatedAt',
            'ogit:openedAt',
            'ogit:priority',
            'ogit:project',
            'ogit:summary',
            'ogit:urgency'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:causes', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:causes', 'ogit.ServiceManagement:Order'),
            ('ogit:causes', 'ogit.ServiceManagement:Ticket'),
            ('ogit:corresponds', 'ogit.ServiceManagement:Service'),
            ('ogit:relates', 'ogit:Contract'),
            ('ogit:relates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:relates', 'ogit.ServiceManagement:Incident'),
            ('ogit:relates', 'ogit.ServiceManagement:Order'),
            ('ogit:relates', 'ogit.ServiceManagement:Problem'),
            ('ogit:relates', 'ogit.ServiceManagement:Ticket'),
            ('ogit:reportedOn', 'ogit.Automation:MARSNode'),
            ('ogit:reportedOn', 'ogit.MARS:Application'),
            ('ogit:reportedOn', 'ogit.MARS:Machine'),
            ('ogit:reportedOn', 'ogit.MARS:Resource'),
            ('ogit:reportedOn', 'ogit.MARS:Software')})
    yield Entity(
        about='ogit.ServiceManagement:Problem',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:problemStatus',
            'ogit.ServiceManagement:resolutionCode',
            'ogit.ServiceManagement:rootCause',
            'ogit.ServiceManagement:solution',
            'ogit.ServiceManagement:workAround',
            'ogit:reportedAt'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit.MARS:Application'),
            ('ogit:affects', 'ogit.MARS:Machine'),
            ('ogit:affects', 'ogit.MARS:Resource'),
            ('ogit:affects', 'ogit.MARS:Software'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit.ServiceManagement:Service'),
            ('ogit:causes', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:causes', 'ogit.ServiceManagement:Problem'),
            ('ogit:complies', 'ogit.ServiceManagement:SLA'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:corresponds', 'ogit.ServiceManagement:Ticket'),
            ('ogit:opens', 'ogit.ServiceManagement:Problem'),
            ('ogit:relates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:relates', 'ogit.ServiceManagement:Incident'),
            ('ogit:relates', 'ogit.ServiceManagement:Order'),
            ('ogit:relates', 'ogit.ServiceManagement:Problem'),
            ('ogit:reportedOn', 'ogit.Automation:MARSNode'),
            ('ogit:reportedOn', 'ogit.MARS:Application'),
            ('ogit:reportedOn', 'ogit.MARS:Machine'),
            ('ogit:reportedOn', 'ogit.MARS:Resource'),
            ('ogit:reportedOn', 'ogit.MARS:Software')})
    yield Entity(
        about='ogit.ServiceManagement:Report',
        parent='ogit:Node',
        optional_attributes={
            'ogit:id',
            'ogit:name',
            'ogit:version'},
        allowed_connections={
            ('ogit:creates', 'ogit.ServiceManagement:Service'),
            ('ogit:generates', 'ogit.Price:Invoice'),
            ('ogit:relates', 'ogit.Automation:MARSNode'),
            ('ogit:relates', 'ogit.MARS:Application'),
            ('ogit:relates', 'ogit.MARS:Machine'),
            ('ogit:relates', 'ogit.MARS:Resource'),
            ('ogit:relates', 'ogit.MARS:Software'),
            ('ogit:uses', 'ogit:Timeseries')})
    yield Entity(
        about='ogit.ServiceManagement:SLA',
        parent='ogit:Node',
        optional_attributes={
            'ogit.ServiceManagement:elapsedTime',
            'ogit.ServiceManagement:leftTime',
            'ogit.ServiceManagement:resolvedInTime',
            'ogit.ServiceManagement:scheduledFinishAt',
            'ogit.ServiceManagement:slaStage',
            'ogit:name',
            'ogit:startedAt'},
        allowed_connections={('ogit:triggers', 'ogit:Penalty')})
    yield Entity(
        about='ogit.ServiceManagement:Service',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit:description',
            'ogit:name',
            'ogit:uri'},
        allowed_connections={
            ('ogit:affects', 'ogit:Person'),
            ('ogit:calls', 'ogit.ServiceManagement:Service'),
            ('ogit:complies', 'ogit.ServiceManagement:SLA'),
            ('ogit:corresponds', 'ogit:CatalogItem'),
            ('ogit:generates', 'ogit.ServiceManagement:Report'),
            ('ogit:implements', 'ogit.Software:Application'),
            ('ogit:opens', 'ogit.ServiceManagement:Incident'),
            ('ogit:opens', 'ogit.ServiceManagement:Ticket'),
            ('ogit:requires', 'ogit.ServiceManagement:Action'),
            ('ogit:requires', 'ogit.ServiceManagement:Service'),
            ('ogit:supports', 'ogit.ServiceManagement:Action')})
    yield Entity(
        about='ogit.ServiceManagement:SubTask',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:customer',
            'ogit.ServiceManagement:resolutionCode',
            'ogit.ServiceManagement:scheduledFinishAt',
            'ogit.ServiceManagement:scheduledStartAt',
            'ogit.ServiceManagement:sourceStatus',
            'ogit.ServiceManagement:targetFinishAt',
            'ogit.ServiceManagement:targetStartAt',
            'ogit.ServiceManagement:taskStatus',
            'ogit:assignedGroup',
            'ogit:description',
            'ogit:effort',
            'ogit:finishedAt',
            'ogit:lastUpdatedAt',
            'ogit:name',
            'ogit:startedAt',
            'ogit:taskLog',
            'ogit:type'},
        allowed_connections={
            ('ogit:affects', 'ogit:ConfigurationItem'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:belongs', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:belongs', 'ogit.ServiceManagement:Incident'),
            ('ogit:belongs', 'ogit.ServiceManagement:Order'),
            ('ogit:belongs', 'ogit.ServiceManagement:Problem'),
            ('ogit:belongs', 'ogit.ServiceManagement:Ticket'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:corresponds', 'ogit:Task'),
            ('ogit:locatedIn', 'ogit:Location'),
            ('ogit:precedes', 'ogit.ServiceManagement:SubTask')})
    yield Entity(
        about='ogit.ServiceManagement:Ticket',
        parent='ogit:Node',
        required_attributes={'ogit:id'},
        optional_attributes={
            'ogit.ServiceManagement:externalTicketId',
            'ogit.ServiceManagement:reportedSource',
            'ogit.ServiceManagement:sourceStatus',
            'ogit.ServiceManagement:ticketId',
            'ogit:closedAt',
            'ogit:createdAt',
            'ogit:description',
            'ogit:impact',
            'ogit:lastUpdatedAt',
            'ogit:openedAt',
            'ogit:priority',
            'ogit:project',
            'ogit:summary',
            'ogit:urgency'},
        allowed_connections={
            ('ogit:affects', 'ogit.Automation:MARSNode'),
            ('ogit:affects', 'ogit.MARS:Application'),
            ('ogit:affects', 'ogit.MARS:Machine'),
            ('ogit:affects', 'ogit.MARS:Resource'),
            ('ogit:affects', 'ogit.MARS:Software'),
            ('ogit:affects', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit:Organization'),
            ('ogit:assignedTo', 'ogit:Person'),
            ('ogit:assignedTo', 'ogit.ServiceManagement:Service'),
            ('ogit:causes', 'ogit.ServiceManagement:Ticket'),
            ('ogit:corresponds', 'ogit.Automation:AutomationIssue'),
            ('ogit:relates', 'ogit.ServiceManagement:Ticket'),
            ('ogit:reportedOn', 'ogit.Automation:MARSNode'),
            ('ogit:reportedOn', 'ogit.MARS:Application'),
            ('ogit:reportedOn', 'ogit.MARS:Machine'),
            ('ogit:reportedOn', 'ogit.MARS:Resource'),
            ('ogit:reportedOn', 'ogit.MARS:Software')})
    yield Entity(
        about='ogit.Software:Application',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit:description',
            'ogit:url',
            'ogit:version'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:complies', 'ogit.ServiceManagement:SLA'),
            ('ogit:contains', 'ogit.Software:SoftwareComponent'),
            ('ogit:generates', 'ogit:Timeseries'),
            ('ogit:relates', 'ogit:License'),
            ('ogit:sends', 'ogit:Notification')})
    yield Entity(
        about='ogit.Software:Connector',
        parent='ogit:Node',
        optional_attributes={
            'ogit:connectorId',
            'ogit:name'},
        allowed_connections={
            ('ogit:creates', 'ogit:ConfigurationItem'),
            ('ogit:creates', 'ogit:Event'),
            ('ogit:creates', 'ogit.ServiceManagement:ChangeRequest'),
            ('ogit:creates', 'ogit.ServiceManagement:Incident')})
    yield Entity(
        about='ogit.Software:Data',
        parent='ogit:Node',
        optional_attributes={'ogit:type'})
    yield Entity(
        about='ogit.Software:SoftwareComponent',
        parent='ogit:Node',
        optional_attributes={'ogit:id'},
        allowed_connections={
            ('ogit:connects', 'ogit.Software:SoftwareComponent'),
            ('ogit:contains', 'ogit.Software:SoftwareComponent'),
            ('ogit:uses', 'ogit.Automation:MARSNode')})
    yield Entity(
        about='ogit.Software:SoftwareConnection',
        parent='ogit:Node',
        optional_attributes={'ogit:type'},
        allowed_connections={
            ('ogit:transfers', 'ogit.Network:NetworkLink'),
            ('ogit:transfers', 'ogit.Software:Data'),
            ('ogit:uses', 'ogit.Software:SoftwareComponent')})
    yield Entity(
        about='ogit.Statistics:AutomationFamily',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={
            'ogit.Automation:marsNodeType',
            'ogit:category',
            'ogit:description'},
        indexed_attributes={
            'ogit:description',
            'ogit:name'})
    yield Entity(
        about='ogit:Status',
        parent='ogit:Node',
        optional_attributes={'ogit:status'},
        allowed_connections={
            ('ogit:relates', 'ogit:Course'),
            ('ogit:relates', 'ogit:Series')})
    yield Entity(
        about='ogit:Subscription',
        parent='ogit:Node',
        optional_attributes={
            'ogit:name',
            'ogit:sourceId',
            'ogit:status',
            'ogit:type'},
        allowed_connections={('ogit:subscribes', 'ogit:Notification')})
    yield Entity(
        about='ogit.Survey:Iteration',
        parent='ogit:Node',
        optional_attributes={
            'ogit:startedAt',
            'ogit:status'},
        allowed_connections={
            ('ogit:belongs', 'ogit.Project:Milestone'),
            ('ogit:belongs', 'ogit.Project:Project'),
            ('ogit:belongs', 'ogit.Survey:Survey')})
    yield Entity(
        about='ogit.Survey:Reply',
        parent='ogit:Node',
        optional_attributes={
            'ogit:comment',
            'ogit:question'},
        allowed_connections={('ogit:belongs', 'ogit.Survey:Iteration')})
    yield Entity(
        about='ogit.Survey:Survey',
        parent='ogit:Node',
        optional_attributes={
            'ogit:category',
            'ogit:description',
            'ogit:question',
            'ogit:schedule',
            'ogit:status',
            'ogit:title',
            'ogit:type'},
        indexed_attributes={
            'ogit:description',
            'ogit:title'},
        allowed_connections={
            ('ogit:belongs', 'ogit:Organization'),
            ('ogit:belongs', 'ogit.Project:Milestone'),
            ('ogit:belongs', 'ogit.Project:Project')})
    yield Entity(
        about='ogit:Tag',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        optional_attributes={'ogit:color'})
    yield Entity(
        about='ogit:Task',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:id',
            'ogit:name',
            'ogit:positionNumber',
            'ogit:question',
            'ogit:response',
            'ogit:status',
            'ogit:type'},
        indexed_attributes={'ogit:name'},
        allowed_connections={('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit:TaskList',
        parent='ogit:Node',
        required_attributes={'ogit:name'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:contains', 'ogit:Task'),
            ('ogit:generates', 'ogit:Timeseries')})
    yield Entity(
        about='ogit:TermsAndConditions',
        parent='ogit:Node',
        required_attributes={
            'ogit:content',
            'ogit:name'},
        optional_attributes={'ogit:description'},
        indexed_attributes={'ogit:name'})
    yield Entity(
        about='ogit:Timeseries',
        parent='ogit:Node',
        optional_attributes={
            'ogit:description',
            'ogit:instance',
            'ogit:isMutable',
            'ogit:name',
            'ogit:unit'},
        indexed_attributes={
            'ogit:description',
            'ogit:instance',
            'ogit:name'})
    yield Entity(
        about='ogit.UserMeta:Filter',
        parent='ogit:Node',
        required_attributes={
            'ogit:content',
            'ogit:name'})
    yield Entity(
        about='ogit.UserMeta:Game',
        parent='ogit:Node',
        allowed_connections={('ogit.UserMeta:asks', 'ogit.UserMeta:Question')})
    yield Entity(
        about='ogit.UserMeta:Preferences',
        parent='ogit:Node')
    yield Entity(
        about='ogit.UserMeta:Question',
        parent='ogit:Node')
    yield Entity(
        about='ogit:Vcard',
        parent='ogit:Node',
        optional_attributes={
            'ogit:addressLocality',
            'ogit:mobilePhone',
            'ogit:phone',
            'ogit:postalCode',
            'ogit:streetAddress'},
        allowed_connections={('ogit:locatedIn', 'ogit:Location')})
    yield Entity(
        about='ogit:VersioningData',
        parent='ogit:Node',
        required_attributes={'ogit:revision'},
        indexed_attributes={'ogit:name'},
        allowed_connections={
            ('ogit:versions', 'ogit.Automation:KnowledgeBundle'),
            ('ogit:versions', 'ogit.Automation:KnowledgeItem')})
    # </editor-fold>
