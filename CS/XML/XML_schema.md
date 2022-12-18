# XML Schema
An XML Schema document describes the structure of an XML document.  
XML Schema can be used as an alternative to the DTDs. It has some advantages over DTD:
- same syntax as XML
- more control of datatypes
- DTD limits expressiveness
- syntax od DTD may differ from XML
- XML Schema Definition (XSD) is the best practice for describing XML doc.
___
## Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- The xmlns:xs specifies that the schema language directives are assigned the xs: namespace prefix -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"> <!-- Declares that all element names in XML instance should be qualified with the namespace -->
  <xs:element name="root">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="element" type="xs:string" maxOccurs="unbounded" minOccurs="0"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```
___
## Elements
A simple element is an XML element that contains no child elements or attributes
`<xs:element name="Identifier" type="Data Type"/>`
Data types:
- xs:string
- xs:decimal
- xs:integer
- xs:boolean
- xs:date
- xs:time

Simple element with default value:
`<xs:element name="genere" type="xs:string" default="Rock"/>`
Simple element with fixed value:
`<xs:element name="genere" type="xs:string" fixed="Rock"/>`

A complex element contains other elements and/or attributes.
```xml
<xs:element name="cd">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="TITLE" type="xs:string"/>
            <xs:element name="ARTIST" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```
___
## Attributes
Attributes are considered simple types(remember simple elements cannot contain attributes!)  
Attribute with default value:
```xml
<xs:attribute name="genre" type="xs:string" defoult="Rock"/>
```
Attribute with fixed value:
```xml
<xs:attribute name="genre" type="xs:string" fied="Rock"/>
```
Attributes are optional, however, the attribute may be required by adding the "use" attribute:
```xml
<xs:attribute name="genre" type="xs:string" use="required"/>
```
___
## Indicators
XML Schema indicators allow us to control how an element is used in the XML document.  
Order indicators(to define the order of the elements):
- All (The <all> indicator specifies that the child elements can appear in any order, and that each child element must occur only once)
- Choice (The <choice> indicator specifies that either one child element or another can occur)
- Sequence (The <sequence> indicator specifies that the child elements must appear in a specific order)

Occurrence indicators (define how often an element can occur):
- maxOccurs (The <maxOccurs> indicator specifies the maximum number of times an element can occur)
- minOccurs (The <minOccurs> indicator specifies the minimum number of times an element can occur)

Group indicators (Group indicators are used to define related sets of elements):
- Group name (Specifies the element group declaration0)
- attributeGroup name (Specifies the attribute group declaration)
___
## Referencing XSD schema in the XML
```xml
<Myschema xmlns:xsi="http://www.Mysite.com"
          xmlns:xis="http://www.w3.org/2001/XMLSchema-instance" 
          xsi:noNamespaceSchemaLocation="http://www.mySite.com schemas/mySchema.xsd">
```
___
### Examples for XML schema
TODO

TODO finish with w3schools

## Sources
- [w3schools](https://www.w3schools.com/XML/default.asp)
- Simon Sez IT, [Learn XML Crash Course: Discover Essential XML Fundamentals](https://www.udemy.com/course/learn-xml-crash-course/)



