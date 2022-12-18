# Extensible Markup Language

- XML is a structural and semantic language, stored in text format, designed for how to store and transmit data. 
- XML doesn't have predefined tags, you define your own tags.
- XML provides for the creation of common information formats allowing the sharing of both the format and the data.
- XML can be used to simplify data storage and sharing. E.g.: XML-formatted data can be easily exchanged between computer and databases systems even if they are incompatible.  
- XML provides for information interchanges (web service).

An XML document's structure is defined by the W3C XML specification AND a Document Type Definition (DTD).  
The fundamental components of an XML are (tags and data):
- Elements mark section of the document (can be nested)
- Attributes provide additional info about an element
- XML is case sensitive
___
## Structure
```xml
<?xml version="1.0" encoding="UTF-8"?> <!-- Declaration line -->
<!-- The prolog of an XML may contain: -->
<!-- XML declaration, if it appears it mustg appear on the very first line with no preceding withe space -->
<!-- Processing instruction which pass parameters to an application defining how to process the XML document -->
<!-- Comments -->
<!-- A document type declaration, specifies: the name of the document element, external DTD, internal DTD -->

<!-- An XML doc. must contain a pair of root tags, and only one pair, of root tags. Is the "parent" element -->
<!-- which contains all other elements. Only one root element per XML document -->
<root attribute="attribute Z">
    <!--An XML element begins from the opening tag to the element's end tag.-->
    <!--Attributes may be included within the start tag, it's value must be quoted with single or double quotes.-->
    <child1 attribute="attribute X">...</child1> 
    <child2>
        <subchild1>...</subchild1>
        <subchild2>...</subchild2>
    </child2>
</root>
<!--The characters "<" and "&" are special and may not be used within an elements data.-->
<!-- To avoid error replace the special characters with an entity reference.-->
<!-- There are 5 predefined entity references in XML:-->
<!-- &lt == < == less than-->
<!-- &gt == > == greater than-->
<!-- &amp == & == ampersand-->
<!-- &apos == ` == apostrophe-->
<!-- &quot == " == quotation mark-->
```
___
### Naming Rules
- Names can contain only letters, numbers, and other characters
- Names must not start with a number or punctuation characters
- Names must not start with the letters xml
- Names cannot contain spaces
- Whitespace is a fundamental building block of good design!
- <!-- This is a comment --> same as in HTML
___
## Example of simple XML
```xml
<?xml version="1.0" encoding="UTF-8"?> <!-- Declaration line -->
<catalog>
    <CD>
        <TITLE>The Dark Side of the Moon</TITLE>
        <ARTIST>Pink Floyd</ARTIST>
        <COUNTRY>USA</COUNTRY>
        <COMPANY>Capital Records</COMPANY>
        <PRICE>12.99</PRICE>
        <COST>5.99</COST>
        <YEAR>1973</YEAR>
    </CD>
    <CD>
        <TITLE>Still got the blues</TITLE>
        <ARTIST>Gary Moore</ARTIST>
        <COUNTRY>UK</COUNTRY>
        <COMPANY>Virgin records</COMPANY>
        <PRICE>10.20</PRICE>
        <YEAR>1990</YEAR>
    </CD>
</catalog>
```
___
## Attributes
The information included in an attribute should describe the data.  
Do not use attribute to represent data!
Attribute limitation:
- Cannot contain multiple values
- Cannot contain tree structures
- Not easily extensible

Use attribute for data about the data:
```xml
<customer id="123"><!-- Must be quoted -->
    ...
</customer>
```
The attribute TYPE field can be set to one of the following:
- An actual value enclosed in quotes
- `#IMPLIED` attribute is optional
- `#REQUIRED` a value must be provided
- `#FIXED value` only the value specified may be used

Default values for an attribute may be provided in the declaration.  
```xml
<!ATTLIST element_name attribute_name CDATA "default_value">
```
___
### Entities
XML ENTITIES may be used as a shorthand for including a particular character or a long string.  
```xml
<!ENITIY name definition>
```
___
### Notations
XML NOTATIONS are used to identify the format of unparsed entities, elements with a notation attribute, or specific processing instruction.  
```xml
<!NOTATION name SYSTEM "external_is">
```
___
### XML namespace
An XML namespace provides a mechanism for avoiding element and attribute name conflicts.  
An XML namespace may be defined using the `xmlns` attribute in the start tag of an element.  
Becomes the default namespace for that element and all child elements contained within that element
```xml
<elmentname xmlns="namespaceURI">
```
___
### Examples with attributes
TODO
___
### Examples for namespaces
TODO

## Sources
- [w3schools](https://www.w3schools.com/XML/default.asp)
- Simon Sez IT, [Learn XML Crash Course: Discover Essential XML Fundamentals](https://www.udemy.com/course/learn-xml-crash-course/)
