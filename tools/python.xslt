<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:dcterms="http://purl.org/dc/terms/"
                xmlns:ogit="http://www.purl.org/ogit/"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
                xmlns:fn="http://www.w3.org/2005/xpath-functions"
                xmlns:a="http://arago.co/"
                xmlns:xml="http://www.w3.org/XML/1998/namespace"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xpath-default-namespace="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
    <xsl:output method="text" byte-order-mark="no" encoding="UTF-8" media-type="palin/text"/>

    <xsl:variable name="PURL_URL" select="'http://www.purl.org/'"/>

    <xsl:template match="rdf:RDF" mode="ns_tree">
        <xsl:param name="all_nss" as="xs:string+"/>
        <xsl:param name="parent_ns" as="xs:string"/>
        <xsl:variable name="child_nss" as="xs:string*" select="$all_nss[a:ns_is_child_of_ns(., $parent_ns)]"/>
        <xsl:variable name="root" select="."/>
        <xsl:for-each select="$child_nss">
            <xsl:sort select="."/>
            <a:namespace>
                <xsl:attribute name="uri" select="."/>
                <xsl:apply-templates select="$root" mode="ns_tree">
                    <xsl:with-param name="all_nss" select="$all_nss"/>
                    <xsl:with-param name="parent_ns" select="."/>
                </xsl:apply-templates>
            </a:namespace>
        </xsl:for-each>
    </xsl:template>

    <xsl:variable name="ns_tree">
        <xsl:variable name="all_nss" as="xs:string+"
                      select="fn:distinct-values(for $node in /rdf:RDF/rdf:Description[exists(@rdf:about)] return a:parent_uris(a:ns_url($node)))"/>
        <a:root>
            <xsl:apply-templates select="/rdf:RDF" mode="ns_tree">
                <xsl:with-param name="all_nss" select="$all_nss"/>
                <xsl:with-param name="parent_ns" select="$PURL_URL"/>
            </xsl:apply-templates>
        </a:root>
    </xsl:variable>

    <xsl:variable name="map">
        <map>
            <entry key="ogit/MRP/kzTCond" value="ogit/MRP/kz_temperature_Cond"/>
            <entry key="ogit/Network/IDSIPS" value="ogit/Network/IDS_IPS"/>
            <entry key="ogit/occurenceCount" value="ogit/occurrence-Count" comment="occurence"/>
            <entry key="ogit/_graphtype" value="ogit/_graph-type"/>
            <entry key="ogit/Credit/CounterpartyMutable" value="ogit/Credit/Counter-party-Mutable"/>
            <entry key="ogit/Timeseries" value="ogit/Time-series"/>

            <entry key="ogit/OSLC-change/inprogress" value="ogit/OSLC-change/in-progress"/>
            <entry key="ogit/OSLC-crtv/vmid" value="ogit/OSLC-crtv/vm-id"/>
            <entry key="ogit/OSLC-crtv/hostid" value="ogit/OSLC-crtv/host-id"/>
            <entry key="ogit/OSLC-perfmon/SqlStatmentFailures" value="ogit/OSLC-perfmon/Sql-Statement-Failures"
                   comment="Statment"/>

            <entry key="ogit/OSLC-perfmon/TimeJCAThreadPoolExhausted"
                   value="ogit/OSLC-perfmon/Time-JCA-Thread-Pool-Exhausted" comment="JCA"/>
            <entry key="ogit/OSLC-perfmon/NetworkIOErrors" value="ogit/OSLC-perfmon/Network-IO-Errors" comment="IO"/>

            <!--            <entry comment="/RDDL/" target="Resource Directory Description Language"/>-->
            <!--            <entry key="ogit/Datacenter/sectionId" value="ogit/Datacenter/sectionId" comment="/Datacenter/" target="Data center"/>-->
            <!--            <entry key="ogit/OSLC-crtv/serverAccessPoint" value="ogit/OSLC-crtv/serverAccessPoint" comment="/OSLC-crtv/" target="Common IT Resource Type Vocabulary"/>-->
            <!--            <entry key="ogit/OSLC-perfmon/VirtualizationMetrics" value="ogit/OSLC-perfmon/VirtualizationMetrics" comment="/OSLC-perfmon/" target="Performance Monitoring"/>-->
            <!--            <entry key="ogit/OSLC-reqman/RequirementCollection" value="ogit/OSLC-reqman/RequirementCollection" comment="/OSLC-reqman/" target="Requirements Management"/>-->
        </map>
    </xsl:variable>

    <xsl:function name="a:escape_java" as="xs:string?">
        <xsl:param name="string" as="xs:string?"/>
        <!-- https://docs.oracle.com/javase/specs/jls/se8/html/jls-3.html#jls-3.10.6 -->
        <xsl:sequence select="
fn:replace(fn:replace(fn:replace(
fn:replace(fn:replace(fn:replace(
$string
, '\\', '\\\\'), '''', '\\'''), '&quot;', '\\&quot;')
, '&#x0D;', '\\r'), '&#x0A;', '\\n'), '&#x09;', '\\t')
"/>
    </xsl:function>

    <xsl:function name="a:escape_python" as="xs:string?">
        <xsl:param name="string" as="xs:string?"/>
        <!-- https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals -->
        <!-- https://www.w3.org/TR/xml/#charsets -->
        <xsl:sequence select="
fn:replace(fn:replace(fn:replace(
fn:replace(fn:replace(fn:replace(
$string
, '\\', '\\\\'), '''', '\\'''), '&quot;', '\\&quot;')
, '&#x0A;', '\\n'), '&#x0D;', '\\r'), '&#x09;', '\\t')
"/>
    </xsl:function>

    <xsl:function name="a:is_attribute" as="xs:boolean*">
        <xsl:param name="node" as="element(Description)"/>
        <!--        <xsl:sequence select="$node/rdfs:subPropertyOf/@rdf:resource = 'http://www.purl.org/ogit/Attribute'"/>-->
        <xsl:sequence select="$node/rdf:type/@rdf:resource = 'http://www.w3.org/2002/07/owl#DatatypeProperty'"/>
    </xsl:function>

    <xsl:function name="a:is_verb" as="xs:boolean*">
        <xsl:param name="node" as="element(Description)"/>
        <!--        <xsl:sequence select="$node/rdfs:subPropertyOf/@rdf:resource = 'http://www.purl.org/ogit/Verb'"/>-->
        <xsl:sequence select="$node/rdf:type/@rdf:resource = 'http://www.w3.org/2002/07/owl#ObjectProperty'"/>
    </xsl:function>

    <xsl:function name="a:is_entity" as="xs:boolean*">
        <xsl:param name="node" as="element(Description)"/>
        <!--        <xsl:sequence select="$node/rdfs:subClassOf/@rdf:resource = 'http://www.purl.org/ogit/Entity'"/>-->
        <xsl:sequence select="$node/rdf:type/@rdf:resource = 'http://www.w3.org/2000/01/rdf-schema#Class'"/>
    </xsl:function>

    <xsl:function name="a:is_ontology" as="xs:boolean">
        <xsl:param name="node" as="element(Description)"/>
        <xsl:sequence select="$node/rdf:type/@rdf:resource = 'http://www.w3.org/2002/07/owl#Ontology'"/>
    </xsl:function>

    <xsl:function name="a:is_annotation" as="xs:boolean">
        <xsl:param name="node" as="element(Description)"/>
        <xsl:sequence select="$node/rdf:type/@rdf:resource = 'http://www.w3.org/2002/07/owl#AnnotationProperty'"/>
    </xsl:function>

    <!--<editor-fold name="fn_namespace">-->
    <xsl:function name="a:in_namespace" as="xs:boolean">
        <xsl:param name="node" as="element(Description)"/>
        <xsl:param name="ns" as="xs:string"/>
        <xsl:sequence select="if (empty($node/@rdf:about)) then false() else a:is_child_of_ns($node/@rdf:about, $ns)"/>
    </xsl:function>

    <xsl:function name="a:ns_is_child_of_ns" as="xs:boolean">
        <xsl:param name="child_ns" as="xs:string"/>
        <xsl:param name="parent_ns" as="xs:string"/>
        <xsl:sequence select="a:is_child_of_ns(fn:replace($child_ns, '/$', ''), $parent_ns)"/>
    </xsl:function>

    <xsl:function name="a:is_child_of_ns" as="xs:boolean">
        <xsl:param name="child_uri" as="xs:string"/>
        <xsl:param name="parent_ns" as="xs:string"/>
        <xsl:variable name="local_name" as="xs:string?" select="fn:substring-after($child_uri, $parent_ns)"/>
        <xsl:variable name="contains_delimiter" select="fn:contains($local_name, '/')"/>
        <!--        <xsl:message select="string-join((string($contains_delimiter), $parent_ns, $child_uri, $local_name), ' -=- ')"/>-->
        <xsl:sequence select="fn:string-length($local_name) gt 0 and fn:not($contains_delimiter)"/>
    </xsl:function>
    <!--</editor-fold>-->

    <xsl:function name="a:to_constant" as="xs:string" xpath-default-namespace="">
        <xsl:param name="url" as="xs:string"/>
        <xsl:variable name="key" select="a:ki_lang(fn:replace($url, '/$', ''))" as="xs:string"/>
        <xsl:variable name="mapped" select="$map/map/entry[@key=$key]/@value" as="xs:string?"/>
        <xsl:variable name="two_char" select="fn:replace($key, '([a-z])([A-Z][a-z])([A-Z][a-z])', '$1_$2_$3')"/>
        <xsl:variable name="any_char" select="fn:replace($two_char, '([a-z])([A-Z][a-z])', '$1_$2')"/>
        <xsl:variable name="acronym_begin" select="fn:replace($any_char, '(/[A-Z]+?)([A-Z][a-z])', '$1_$2')"/>
        <xsl:variable name="acronym_end" select="fn:replace($acronym_begin, '([a-z])([A-Z][A-Z]+)$', '$1_$2')"/>
        <xsl:variable name="snake_case" select="$acronym_end"/>
        <xsl:variable name="ki_lang_name" select="if(fn:exists($mapped)) then $mapped else $snake_case" as="xs:string"/>
        <xsl:sequence select="fn:upper-case(fn:translate($ki_lang_name, '/-', '__'))"/>
    </xsl:function>

    <xsl:function name="a:ns_url_to_prefix" as="xs:string" xpath-default-namespace="">
        <xsl:param name="url" as="xs:string"/>
        <xsl:variable name="relative_uri" select="a:ki_lang(fn:replace($url, '/$', ''))" as="xs:string"/>
        <xsl:variable name="tokens" select="fn:tokenize($relative_uri, '/')"/>
        <xsl:variable name="prefix" select="string-join($tokens, '.')"/>
        <xsl:sequence select="$prefix"/>
    </xsl:function>

    <xsl:function name="a:url_to_prefixed_name" as="xs:string" xpath-default-namespace="">
        <xsl:param name="url" as="xs:string"/>
        <xsl:variable name="relative_uri" select="a:ki_lang(fn:replace($url, '/$', ''))" as="xs:string"/>
        <xsl:variable name="tokens" select="fn:tokenize($relative_uri, '/')"/>
        <xsl:variable name="prefix" select="string-join($tokens[position() lt fn:last()], '.')"/>
        <xsl:variable name="local_name" select="$tokens[position() eq fn:last()]"/>
        <xsl:sequence select="string-join(($prefix, $local_name), ':')"/>
    </xsl:function>

    <xsl:function name="a:constant_to_class_name" as="xs:string">
        <xsl:param name="constant" as="xs:string"/>
        <xsl:variable name="tokens" select="fn:tokenize($constant, '_')"/>
        <xsl:variable name="capped_tokens"
                      select="for $t in $tokens return concat(fn:upper-case(substring($t, 1, 1)), lower-case(substring($t, 2)))"/>
        <xsl:sequence select="string-join($capped_tokens, '')"/>
    </xsl:function>

    <xsl:function name="a:ki_lang" xpath-default-namespace="">
        <xsl:param name="url" as="xs:string"/>
        <xsl:sequence select="fn:substring-after($url, $PURL_URL)"/>
    </xsl:function>

    <xsl:function name="a:ogit_ns_prefix">
        <xsl:param name="node" as="element()"/>
        <xsl:sequence select="fn:starts-with(fn:prefix-from-QName(fn:node-name($node)), 'ogit')"/>
    </xsl:function>

    <xsl:function name="a:ns_url" as="xs:string">
        <xsl:param name="node" as="element(Description)"/>
        <xsl:sequence
                select="concat(string-join(fn:tokenize($node/@rdf:about, '/')[position()!=fn:last()], '/'), '/')"/>
    </xsl:function>

    <xsl:function name="a:uri_to_ogit_prefix" as="xs:string">
        <xsl:param name="string" as="xs:string"/>
        <xsl:sequence select="fn:translate(fn:replace(fn:substring-after($string, $PURL_URL), '/$', ''), '/', '.')"/>
    </xsl:function>

    <xsl:template match="rdf:Description[exists(@rdf:nodeID)]" mode="collection">
        <xsl:apply-templates select="child::element()[a:ogit_ns_prefix(.)]" mode="collection_entry"/>
        <xsl:apply-templates select="../rdf:Description[@rdf:about=current()/rdf:first/@rdf:resource]"
                             mode="collection_entry"/>
        <xsl:apply-templates select="../rdf:Description[@rdf:nodeID=current()/rdf:first/@rdf:nodeID]"
                             mode="collection"/>
        <xsl:apply-templates select="../rdf:Description[@rdf:nodeID=current()/rdf:rest/@rdf:nodeID]" mode="collection"/>
    </xsl:template>

    <xsl:function name="a:resolveCollection" as="element()*">
        <xsl:param name="root" as="element()?"/>
        <xsl:if test="fn:exists($root)">
            <xsl:sequence select="$root/element()[a:ogit_ns_prefix(.)]"/>
            <xsl:sequence select="$root/../rdf:Description[@rdf:about=$root/rdf:first/@rdf:resource]"/>
            <xsl:sequence
                    select="a:resolveCollection($root/../rdf:Description[@rdf:nodeID=$root/rdf:first/@rdf:nodeID])"/>
            <xsl:sequence
                    select="a:resolveCollection($root/../rdf:Description[@rdf:nodeID=$root/rdf:rest/@rdf:nodeID])"/>
        </xsl:if>
    </xsl:function>

    <!--<editor-fold name="resolver">-->
    <xsl:function name="a:resolveNode" as="element(Description)">
        <xsl:param name="node" as="element()"/>
        <xsl:variable name="id" select="$node/@rdf:nodeID"/>
        <xsl:sequence select="$node/../../rdf:Description[@rdf:nodeID=$id]"/>
    </xsl:function>

    <xsl:function name="a:resolveConnectionVerb" as="element(Description)">
        <xsl:param name="node" as="element()"/>
        <xsl:variable name="uri" select="concat(namespace-uri($node), local-name($node))"/>
        <xsl:sequence select="$node/../../rdf:Description[@rdf:about=$uri]"/>
    </xsl:function>

    <xsl:function name="a:resolveByAboutUri" as="element(Description)">
        <xsl:param name="node" as="element()"/>
        <xsl:param name="uri" as="xs:string"/>
        <xsl:sequence select="$node/../../rdf:Description[@rdf:about=$uri]"/>
    </xsl:function>

    <xsl:function name="a:resolveConnectionEntity" as="element(Description)">
        <xsl:param name="node" as="element()"/>
        <xsl:variable name="uri" select="$node/@rdf:resource"/>
        <xsl:sequence select="$node/../../rdf:Description[@rdf:about=$uri]"/>
    </xsl:function>
    <!--</editor-fold>-->

    <!--<editor-fold name="collection entries">-->
    <xsl:template match="*[a:ogit_ns_prefix(.)]" mode="collection_entry">
        <xsl:variable name="verb_uri" select="concat(namespace-uri(current()), local-name(current()))"/>
        <xsl:variable name="verb" select="a:resolveConnectionVerb(.)" as="element()?"/>
        <xsl:variable name="entity_uri" select="current()/@rdf:resource"/>
        <xsl:variable name="entity" select="a:resolveConnectionEntity(.)" as="element()?"/>
        <xsl:if test="empty($verb)">
            <xsl:message terminate="yes">
                <xsl:text>Failed to resolve verb: </xsl:text>
                <xsl:value-of select="$verb_uri"/>
            </xsl:message>
        </xsl:if>
        <xsl:if test="empty($entity)">
            <xsl:message terminate="yes">
                <xsl:text>For verb: </xsl:text>
                <xsl:value-of select="$verb_uri"/>
                <xsl:text>&#x0A;</xsl:text>
                <xsl:text>Failed to resolve entity: </xsl:text>
                <xsl:value-of select="$entity_uri"/>
            </xsl:message>
        </xsl:if>

        <xsl:if test="fn:last() gt 1">
            <xsl:text>&#x0A;        </xsl:text>
        </xsl:if>
        <xsl:text>AllowedConnection(</xsl:text>
        <xsl:value-of select="concat('Verb.', a:to_constant($verb/@rdf:about))"/>
        <xsl:text>, </xsl:text>
        <xsl:value-of select="a:to_constant($entity/@rdf:about)"/>
        <xsl:text>)</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="*[a:ogit_ns_prefix(.)]" mode="collection_entry_factory">
        <xsl:variable name="verb_uri" select="concat(namespace-uri(current()), local-name(current()))"/>
        <xsl:variable name="verb" select="a:resolveConnectionVerb(.)" as="element()?"/>
        <xsl:variable name="entity_uri" select="current()/@rdf:resource"/>
        <xsl:variable name="entity" select="a:resolveConnectionEntity(.)" as="element()?"/>
        <xsl:if test="empty($verb)">
            <xsl:message terminate="yes">
                <xsl:text>Failed to resolve verb: </xsl:text>
                <xsl:value-of select="$verb_uri"/>
            </xsl:message>
        </xsl:if>
        <xsl:if test="empty($entity)">
            <xsl:message terminate="yes">
                <xsl:text>For verb: </xsl:text>
                <xsl:value-of select="$verb_uri"/>
                <xsl:text>&#x0A;</xsl:text>
                <xsl:text>Failed to resolve entity: </xsl:text>
                <xsl:value-of select="$entity_uri"/>
            </xsl:message>
        </xsl:if>

        <xsl:if test="fn:last() gt 1">
            <xsl:text>&#x0A;        </xsl:text>
        </xsl:if>
        <xsl:text>('</xsl:text>
        <xsl:value-of select="a:escape_python(a:url_to_prefixed_name($verb/@rdf:about))"/>
        <xsl:text>', '</xsl:text>
        <xsl:value-of select="a:escape_python(a:url_to_prefixed_name($entity/@rdf:about))"/>
        <xsl:text>')</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="rdf:Description[exists(@rdf:about)]" mode="collection_entry">
        <xsl:if test="fn:last() gt 1">
            <xsl:text>&#x0A;        </xsl:text>
        </xsl:if>
        <xsl:text>'</xsl:text>
        <xsl:value-of select="a:escape_python(a:url_to_prefixed_name(@rdf:about))"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>
    <!--</editor-fold>-->

    <!--<editor-fold name="namespace alias classes">-->
    <xsl:template match="rdf:RDF" mode="ns_classes">
        <xsl:variable name="nodes"
                      select="rdf:Description[exists(@rdf:about) and exists(rdfs:label) and not(a:is_ontology(.))]"/>
        <xsl:variable name="uris"
                      select="fn:distinct-values(for $node in $nodes return a:parent_uris(a:ns_url($node)))"/>
        <xsl:variable name="root" select="."/>
        <xsl:for-each select="$uris">
            <xsl:sort select="."/>
            <xsl:variable name="class_name" select="a:constant_to_class_name(a:to_constant(.))"/>
            <xsl:result-document href="generated/{$class_name}.py" method="text" byte-order-mark="no" encoding="UTF-8">
                <xsl:apply-templates select="$root" mode="ns_class">
                    <xsl:with-param name="ns_uri" select="."/>
                </xsl:apply-templates>
            </xsl:result-document>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="rdf:RDF" mode="ns_class">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:variable name="nodes"
                      select="rdf:Description[a:in_namespace(., $ns_uri) and (a:is_attribute(.) or a:is_verb(.) or a:is_entity(.))]"/>
        <xsl:variable name="class_name" select="a:constant_to_class_name(a:to_constant($ns_uri))"/>
        <xsl:text>package co.arago.ontology

import co.arago.ontology.Attribute as OuterAttribute
import co.arago.ontology.Entity as OuterEntity
import co.arago.ontology.Namespace as OuterNamespace
import co.arago.ontology.Verb as OuterVerb

import groovy.transform.CompileStatic

@SuppressWarnings('unused')
@CompileStatic
</xsl:text>
        <xsl:text>class </xsl:text>
        <xsl:value-of select="$class_name"/>
        <xsl:text> {&#x0A;</xsl:text>
        <xsl:variable name="child_namespaces" select="$ns_tree//a:namespace[@uri=$ns_uri]/a:namespace"/>
        <xsl:if test="fn:exists($child_namespaces)">
            <xsl:text>    static final class Namespace</xsl:text>
            <xsl:text> {&#x0A;</xsl:text>
            <xsl:apply-templates select="$child_namespaces" mode="ns_class">
                <xsl:sort select="@uri"/>
                <xsl:with-param name="ns_uri" select="$ns_uri"/>
            </xsl:apply-templates>
            <xsl:text>    }&#x0A;</xsl:text>
        </xsl:if>
        <xsl:variable name="attributes" select="$nodes[a:is_attribute(.)]"/>
        <xsl:if test="fn:exists($attributes)">
            <xsl:text>    static final class Attribute</xsl:text>
            <xsl:text> {&#x0A;</xsl:text>
            <xsl:apply-templates select="$attributes" mode="ns_class">
                <xsl:sort select="@rdf:about"/>
                <xsl:with-param name="ns_uri" select="$ns_uri"/>
            </xsl:apply-templates>
            <xsl:text>    }&#x0A;</xsl:text>
        </xsl:if>
        <xsl:variable name="verbs" select="$nodes[a:is_verb(.)]"/>
        <xsl:if test="fn:exists($verbs)">
            <xsl:text>    static final class Verb</xsl:text>
            <xsl:text> {&#x0A;</xsl:text>
            <xsl:apply-templates select="$verbs" mode="ns_class">
                <xsl:sort select="@rdf:about"/>
                <xsl:with-param name="ns_uri" select="$ns_uri"/>
            </xsl:apply-templates>
            <xsl:text>    }&#x0A;</xsl:text>
        </xsl:if>
        <xsl:variable name="entities" select="$nodes[a:is_entity(.)]"/>
        <xsl:if test="fn:exists($entities)">
            <xsl:text>    static final class Entity</xsl:text>
            <xsl:text> {&#x0A;</xsl:text>
            <xsl:apply-templates select="$entities" mode="ns_class">
                <xsl:sort select="@rdf:about"/>
                <xsl:with-param name="ns_uri" select="$ns_uri"/>
            </xsl:apply-templates>
            <xsl:text>    }&#x0A;</xsl:text>
        </xsl:if>
        <xsl:apply-templates select="$nodes" mode="ns_check">
            <xsl:sort select="@rdf:about"/>
            <xsl:with-param name="ns_uri" select="$ns_uri"/>
        </xsl:apply-templates>
        <xsl:text>}&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="a:namespace" mode="ns_class">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:text>        public static final OuterNamespace </xsl:text>
        <xsl:value-of select="fn:substring-after(a:to_constant(@uri), concat(a:to_constant($ns_uri), '_'))"/>
        <xsl:text> = </xsl:text>
        <xsl:text>OuterNamespace.</xsl:text>
        <xsl:value-of select="a:to_constant(@uri)"/>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_attribute(.)]" mode="ns_class">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:text>        public static final OuterAttribute </xsl:text>
        <xsl:value-of select="fn:substring-after(a:to_constant(@rdf:about), concat(a:to_constant($ns_uri), '_'))"/>
        <xsl:text> = </xsl:text>
        <xsl:text>OuterAttribute.</xsl:text>
        <xsl:value-of select="a:to_constant(@rdf:about)"/>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_verb(.)]" mode="ns_class">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:text>        public static final OuterVerb </xsl:text>
        <xsl:value-of select="fn:substring-after(a:to_constant(@rdf:about), concat(a:to_constant($ns_uri), '_'))"/>
        <xsl:text> = </xsl:text>
        <xsl:text>OuterVerb.</xsl:text>
        <xsl:value-of select="a:to_constant(@rdf:about)"/>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_entity(.)]" mode="ns_class">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:text>        public static final OuterEntity </xsl:text>
        <xsl:value-of select="fn:substring-after(a:to_constant(@rdf:about), concat(a:to_constant($ns_uri), '_'))"/>
        <xsl:text> = </xsl:text>
        <xsl:text>OuterEntity.</xsl:text>
        <xsl:value-of select="a:to_constant(@rdf:about)"/>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description" mode="ns_check">
        <xsl:param name="ns_uri" as="xs:string"/>
        <xsl:variable name="about" select="@rdf:about"/>
        <xsl:variable name="preceding"
                      select="preceding-sibling::rdf:Description[lower-case(@rdf:about) = lower-case($about)]"/>
        <xsl:variable name="following"
                      select="following-sibling::rdf:Description[lower-case(@rdf:about) = lower-case($about)]"/>
        <xsl:if test="fn:empty($following) and fn:exists($preceding)">
            <xsl:message>
                <xsl:text>WARN: case insensitive QName clash! </xsl:text>
                <xsl:for-each select="(., $preceding)">
                    <xsl:choose>
                        <xsl:when test="a:is_attribute(.)">
                            <xsl:text>Attribute</xsl:text>
                        </xsl:when>
                        <xsl:when test="a:is_verb(.)">
                            <xsl:text>Verb</xsl:text>
                        </xsl:when>
                        <xsl:when test="a:is_entity(.)">
                            <xsl:text>Entity</xsl:text>
                        </xsl:when>
                        <xsl:otherwise/>
                    </xsl:choose>
                    <xsl:text>{</xsl:text>
                    <xsl:value-of select="@rdf:about"/>
                    <xsl:text>}</xsl:text>
                    <xsl:if test="position()!=fn:last()">
                        <xsl:text> with </xsl:text>
                    </xsl:if>
                </xsl:for-each>
            </xsl:message>
        </xsl:if>
    </xsl:template>
    <!--</editor-fold>-->

    <xsl:function name="a:parent_uris" as="xs:string*">
        <xsl:param name="uri" as="xs:string"/>
        <xsl:variable name="path" select="fn:substring-after($uri, $PURL_URL)" as="xs:string"/>
        <xsl:variable name="path_tokens" select="fn:tokenize($path, '/')[position()!=last()]" as="xs:string*"/>
        <xsl:variable name="paths"
                      select="for $i in 1 to count($path_tokens) return string-join($path_tokens[position() le $i], '/')"
                      as="xs:string*"/>
        <xsl:variable name="uris" select="for $path in $paths return concat($PURL_URL, $path, '/')" as="xs:string*"/>
        <xsl:sequence select="$uris"/>
    </xsl:function>

    <!--<editor-fold name="namespace instances">-->
    <xsl:template match="rdf:RDF" mode="instance_namespaces_data">
        <xsl:variable
                name="nodes" as="element(rdf:Description)*"
                select="rdf:Description[exists(@rdf:about) and exists(rdfs:label) and not(a:is_ontology(.))]"/>
        <xsl:variable
                name="namespace_uris" as="xs:string*"
                select="fn:distinct-values(for $node in $nodes return a:parent_uris(a:ns_url($node)))"/>
        <xsl:for-each select="$namespace_uris">
            <xsl:sort select="."/>
            <xsl:call-template name="instance_namespace_data">
                <xsl:with-param name="uri" select="."/>
            </xsl:call-template>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="rdf:RDF" mode="enum_member">
        <xsl:variable
                name="nodes" as="element(rdf:Description)*"
                select="rdf:Description[exists(@rdf:about) and exists(rdfs:label) and not(a:is_ontology(.))]"/>
        <xsl:variable
                name="namespace_uris" as="xs:string*"
                select="fn:distinct-values(for $node in $nodes return a:parent_uris(a:ns_url($node)))"/>
        <xsl:for-each select="$namespace_uris">
            <xsl:sort select="."/>
            <xsl:call-template name="namespace_enum_member">
                <xsl:with-param name="uri" select="."/>
            </xsl:call-template>
        </xsl:for-each>
    </xsl:template>

    <xsl:template name="instance_namespace_data">
        <xsl:param name="uri" as="xs:string"/>
        <xsl:text>yield </xsl:text>
        <xsl:text>Namespace(</xsl:text>
        <xsl:call-template name="namespace_kw_arg">
            <xsl:with-param name="uri" select="$uri"/>
        </xsl:call-template>
        <xsl:text>)&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template name="namespace_enum_member">
        <xsl:param name="uri" as="xs:string"/>
        <xsl:variable name="const" select="a:to_constant($uri)"/>
        <xsl:value-of select="$const"/>
        <xsl:text> = </xsl:text>
        <xsl:text>m['</xsl:text>
        <xsl:value-of select="a:escape_python($const)"/>
        <xsl:text>']</xsl:text>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template name="namespace_kw_arg">
        <xsl:param name="uri" as="xs:string"/>
        <xsl:text>&#x0A;    prefix='</xsl:text>
        <xsl:value-of select="a:escape_python(a:ns_url_to_prefix($uri))"/>
        <xsl:text>'</xsl:text>
    </xsl:template>
    <!--</editor-fold>-->

    <xsl:template match="rdf:Description[a:is_attribute(.)]" mode="instance_data">
        <xsl:text>yield </xsl:text>
        <xsl:text>Attribute(</xsl:text>
        <xsl:apply-templates select="(
            @rdf:about,
            rdfs:label,
            dcterms:description,
            dcterms:created,
            dcterms:modified,
            dcterms:valid,
            ogit:hide,
            dcterms:creator,
            ogit:deleter,
            ogit:admin-contact,
            ogit:tech-contact,
            ogit:validation-type,
            ogit:validation-parameter
        )" mode="kw_arg"/>
        <xsl:text>)&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_verb(.)]" mode="instance_data">
        <xsl:text>yield </xsl:text>
        <xsl:text>Verb(</xsl:text>
        <xsl:apply-templates select="(
            @rdf:about,
            rdfs:label,
            dcterms:description,
            dcterms:created,
            dcterms:modified,
            dcterms:valid,
            ogit:hide,
            dcterms:creator,
            ogit:deleter,
            ogit:admin-contact,
            ogit:tech-contact,
            ogit:cardinality
        )" mode="kw_arg"/>
        <xsl:text>)&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_entity(.)]" mode="instance_data">
        <xsl:text>yield </xsl:text>
        <xsl:text>Entity(</xsl:text>
        <xsl:apply-templates select="(
            @rdf:about,
            rdfs:label,
            dcterms:description,
            dcterms:created,
            dcterms:modified,
            dcterms:valid,
            ogit:hide,
            dcterms:creator,
            ogit:deleter,
            ogit:admin-contact,
            ogit:tech-contact,
            ogit:scope
        )" mode="kw_arg"/>
        <xsl:text>)&#x0A;</xsl:text>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_entity(.)]" mode="instance_refs">
        <xsl:variable name="nodes" select="(
            @rdf:about,
            ogit:parent[@rdf:resource != 'http://www.w3.org/1999/02/22-rdf-syntax-ns#nil'],
            ogit:mandatory-attributes[fn:exists(@rdf:nodeID)],
            ogit:optional-attributes[fn:exists(@rdf:nodeID)],
            ogit:indexed-attributes[fn:exists(@rdf:nodeID)],
            ogit:allowed[fn:exists(@rdf:nodeID)]
        )" as="node()+"/>
        <xsl:if test="count($nodes) gt 1">
            <xsl:text>yield </xsl:text>
            <xsl:text>Entity(</xsl:text>
            <xsl:apply-templates select="$nodes" mode="kw_arg"/>
            <xsl:text>)&#x0A;</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="rdf:Description[a:is_entity(.) or a:is_verb(.) or a:is_attribute(.)]" mode="enum_member">
        <xsl:variable name="const" select="a:to_constant(@rdf:about)"/>
        <xsl:value-of select="$const"/>
        <xsl:text> = </xsl:text>
        <xsl:text>m['</xsl:text>
        <xsl:value-of select="a:escape_python($const)"/>
        <xsl:text>']</xsl:text>
        <xsl:text>&#x0A;</xsl:text>
    </xsl:template>

    <!--<editor-fold name="properties">-->
    <xsl:template match="@rdf:about" mode="kw_arg">
        <xsl:text>&#x0A;    about='</xsl:text>
        <xsl:value-of select="a:escape_python(a:url_to_prefixed_name(string()))"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="rdfs:label" mode="kw_arg">
        <xsl:text>&#x0A;    label='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="dcterms:description" mode="kw_arg">
        <xsl:text>&#x0A;    description='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="dcterms:created" mode="kw_arg">
        <xsl:text>&#x0A;    created_at='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="dcterms:valid" mode="kw_arg">
        <xsl:text>&#x0A;    valid='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="dcterms:modified" mode="kw_arg">
        <xsl:text>&#x0A;    modified_at='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:hide" mode="raw_value">
        <xsl:variable name="value" select="lower-case(normalize-space(text()))"/>
        <xsl:choose>
            <xsl:when test="$value='true' or $value='yes' or $value='y' or $value='t' or $value='1'">
                <xsl:text>True</xsl:text>
            </xsl:when>
            <xsl:when test="$value='false' or $value='no' or $value='n' or $value='f' or $value='0'">
                <xsl:text>False</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>None</xsl:text>
                <xsl:message>
                    <xsl:text>WARN: </xsl:text>
                    <xsl:text>Ignoring ogit:hide value "</xsl:text>
                    <xsl:value-of select="text()"/>
                    <xsl:text>" since it cannot be cast to boolean one.</xsl:text>
                </xsl:message>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ogit:hide" mode="kw_arg">
        <xsl:text>&#x0A;    hide=</xsl:text>
        <xsl:apply-templates select="." mode="raw_value"/>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="dcterms:creator" mode="kw_arg">
        <xsl:text>&#x0A;    created_by='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:deleter" mode="kw_arg">
        <xsl:text>&#x0A;    deleted_by='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:admin-contact" mode="kw_arg">
        <xsl:text>&#x0A;    admin_contact='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:tech-contact" mode="kw_arg">
        <xsl:text>&#x0A;    tech_contact='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:validation-type" mode="raw_value">
        <xsl:variable name="value" select="lower-case(normalize-space(text()))"/>
        <xsl:choose>
            <xsl:when test="$value='fixed'">
                <xsl:text>ValidatorType.FIXED</xsl:text>
            </xsl:when>
            <xsl:when test="$value='regex'">
                <xsl:text>ValidatorType.REGEX</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>None</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ogit:validation-type" mode="kw_arg">
        <xsl:text>&#x0A;    validation_type=</xsl:text>
        <xsl:apply-templates select="." mode="raw_value"/>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:validation-parameter" mode="kw_arg">
        <xsl:text>&#x0A;    validation_parameter='</xsl:text>
        <xsl:value-of select="a:escape_python(text())"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:scope" mode="raw_value">
        <xsl:variable name="value" select="lower-case(normalize-space(text()))"/>
        <xsl:choose>
            <xsl:when test="$value='nto'">
                <xsl:text>Scope.NTO</xsl:text>
            </xsl:when>
            <xsl:when test="$value='sgo'">
                <xsl:text>Scope.SGO</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>None</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ogit:scope" mode="kw_arg">
        <xsl:text>&#x0A;    scope=</xsl:text>
        <xsl:apply-templates select="." mode="raw_value"/>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:parent" mode="kw_arg">
        <xsl:text>&#x0A;    parent='</xsl:text>
        <xsl:value-of select="a:url_to_prefixed_name(@rdf:resource)"/>
        <xsl:text>'</xsl:text>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:cardinality" mode="raw_value">
        <xsl:variable name="value" select="lower-case(normalize-space(text()))"/>
        <xsl:choose>
            <xsl:when test="$value='many2many'">
                <xsl:text>Cardinality.MANY_TO_MANY</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>None</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="ogit:cardinality" mode="kw_arg">
        <xsl:text>&#x0A;    cardinality=</xsl:text>
        <xsl:apply-templates select="." mode="raw_value"/>
        <xsl:if test="position()!=fn:last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>
    <!--</editor-fold>-->

    <!--<editor-fold name="attributes">-->
    <xsl:template match="ogit:mandatory-attributes" mode="kw_arg">
        <xsl:variable name="nodes" select="a:resolveCollection(a:resolveNode(.))"/>
        <xsl:if test="fn:exists($nodes)">
            <xsl:text>&#x0A;    required_attributes={</xsl:text>
            <xsl:apply-templates select="$nodes" mode="collection_entry">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
            <xsl:text>}</xsl:text>
            <xsl:if test="position()!=fn:last()">
                <xsl:text>,</xsl:text>
            </xsl:if>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:optional-attributes" mode="kw_arg">
        <xsl:variable name="nodes" select="a:resolveCollection(a:resolveNode(.))"/>
        <xsl:if test="fn:exists($nodes)">
            <xsl:text>&#x0A;    optional_attributes={</xsl:text>
            <xsl:apply-templates select="$nodes" mode="collection_entry">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
            <xsl:text>}</xsl:text>
            <xsl:if test="position()!=fn:last()">
                <xsl:text>,</xsl:text>
            </xsl:if>
        </xsl:if>
    </xsl:template>

    <xsl:template match="ogit:indexed-attributes" mode="kw_arg">
        <xsl:variable name="nodes" select="a:resolveCollection(a:resolveNode(.))"/>
        <xsl:if test="fn:exists($nodes)">
            <xsl:text>&#x0A;    indexed_attributes={</xsl:text>
            <xsl:apply-templates select="$nodes" mode="collection_entry">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
            <xsl:text>}</xsl:text>
            <xsl:if test="position()!=fn:last()">
                <xsl:text>,</xsl:text>
            </xsl:if>
        </xsl:if>
    </xsl:template>
    <!--</editor-fold>-->

    <!--<editor-fold name="verbs">-->
    <xsl:template match="ogit:allowed" mode="kw_arg">
        <xsl:variable name="nodes" select="a:resolveCollection(a:resolveNode(.))"/>
        <xsl:if test="fn:exists($nodes)">
            <xsl:text>&#x0A;    allowed_connections={</xsl:text>
            <xsl:apply-templates select="$nodes" mode="collection_entry_factory">
                <xsl:sort select="a:resolveConnectionVerb(.)/@rdf:about" stable="yes"/>
                <xsl:sort select="a:resolveConnectionEntity(.)/@rdf:about"/>
            </xsl:apply-templates>
            <xsl:text>}</xsl:text>
            <xsl:if test="position()!=fn:last()">
                <xsl:text>,</xsl:text>
            </xsl:if>
        </xsl:if>
    </xsl:template>
    <!--</editor-fold>-->

    <xsl:template match="rdf:RDF">
        <xsl:result-document href="Namespace.data.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="." mode="instance_namespaces_data"/>
        </xsl:result-document>
        <xsl:result-document href="Namespace.members.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="." mode="enum_member"/>
        </xsl:result-document>
        <xsl:result-document href="Attribute.data.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_attribute(.)]" mode="instance_data">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Attribute.members.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_attribute(.)]" mode="enum_member">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Verb.data.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_verb(.)]" mode="instance_data">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Verb.members.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_verb(.)]" mode="enum_member">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Entity.data.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_entity(.)]" mode="instance_data">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Entity.refs.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_entity(.)]" mode="instance_refs">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:result-document href="Entity.members.generated.py" method="text" byte-order-mark="no" encoding="UTF-8">
            <xsl:apply-templates select="rdf:Description[a:is_entity(.)]" mode="enum_member">
                <xsl:sort select="@rdf:about"/>
            </xsl:apply-templates>
        </xsl:result-document>
        <xsl:apply-templates select="." mode="ns_classes"/>
    </xsl:template>

    <xsl:template match="/">
        <!-- owl:versionInfo -->
        <!--        <xsl:message select="$ns_tree"/>-->
        <xsl:apply-templates select="/rdf:RDF"/>
    </xsl:template>
</xsl:stylesheet>