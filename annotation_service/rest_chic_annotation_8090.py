#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

from time import gmtime, strftime

resource_file = 'Dawn_model_resource_8090.xml'
tree = ET.parse(resource_file)
root = tree.getroot()

#

resource_hypomodel ='Hypomodel';
resource_hypermodel='Hypermodel';
resource_dataset   ='Dataset';

base_path   = '/chic'
models_path = '/models'
mdata_path  = '/data'
resource_path='/resource'

http_content_type = 'xml';
urls = (
        #'/users', 'list_users',
        #'/users/(.*)', 'get_user',
        models_path, 'get_model_list',
        #models_path+'/.*', 'get_model',
        base_path+'/resource/(.*)/Description', 'get_description',
        base_path+'/resource/(.*)/xml', 'get_resource_xml',
        base_path+'/resource/(.*)/CommonMetadata/(.*)', 'get_resource_id_common_metadata_by_name',
        base_path+'/resource/(.*)/SpecificMetadata/(.*)', 'get_resource_id_specific_metadata_by_name',
        base_path+'/resource/(.*)/metadata/(.*)', 'get_resource_id_metadata_by_name',
        base_path+'/resource/(.*)/Tags', 'add_resource_id_tags',
        base_path+'/resource/(.*)/metadata/(.*)/xml', 'get_resource_id_metadata_by_name',
        base_path+'/resource/(.*)', 'get_resource_xml',
        #base_path+'/data/resource/(.?)', 'get_resource_xml',
        #base_path+'/model/resource/(.?)/xml', 'get_resource_xml',
)

app = web.application(urls, globals())







class add_resource_id_tags:
  def PUT(self, resource_id):
    print('add_resource_id_tags, resource_id='+str(resource_id));
    print(web.data());

    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
          common_metadata  = child.find('CommonMetadata');
          old_tags  = common_metadata.find('Tags');
          try:    
            new_tags  = str(web.data());
            # test = "<test>pippo</test>";
            # old_tags.text = ET.fromstring(test);
            
            common_metadata.find('Tags').clear();
            common_metadata.find('Tags').append(ET.fromstring(new_tags));
            #old_tags.text = new_tags;
            #print(str(child))
            print(str(ET.tostring(child, 'utf-8', method='xml')));
            tree.write(resource_file);
          except:
            print('exception raised');
            common_metadata.find('Tags').append(old_tags);
            app.notfound();
            return;


# Return metadata by name from metadata
class get_resource_id_metadata_by_name:
  def GET(self, resource_id, metadata_name):
    web.header('Content-Type', 'text/xml');
    print('get_resource_id_metadata_by_name');
    print("getting resourceID="+str(resource_id)+" metadata="+str(metadata_name)+'content_type='+str(http_content_type));
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        resource = child;
        common_metadata   = resource.find('CommonMetadata');
        specific_metadata = resource.find('SpecificMetadata');
        
        resource_type = str(common_metadata.find('Type').text).strip();
        
        # Resource specific metadata to restrict search in case of redundant
        # tag/element names
        resource_specific_metadata = specific_metadata.find(resource_type);
        
        print('resource_specific_metadata='+str(ET.tostring(resource_specific_metadata, 'utf-8', method='xml')));
        
        if resource_type == resource_hypermodel:
          print("switch case\n") ;
        
        elif resource_type == resource_hypermodel:
          print("switch case\n"+resource_hypermodel) ;
        elif resource_type == resource_dataset:
          print("switch case\n"+resource_dataset) ;
        
        print('resource_type='+resource_type);
        
        try:
          xml_element_specific = resource_specific_metadata.find(metadata_name);
          xml_element_common   = common_metadata.find(metadata_name);
          
          if ET.iselement(xml_element_common):
            output = ET.tostring(xml_element_common, 'utf-8', method='xml')
            xml_element = xml_element_common
          elif ET.iselement(xml_element_specific):
            output = ET.tostring(xml_element_specific, 'utf-8', method='xml')
            xml_element =xml_element_specific;
          
          
          print('output='+str(output));
          
          if http_content_type != 'xml':
            output == xml_element.text;
          
          #description = common_meta_data.find('Description');
          #output = ET.tostring(description, 'utf-8', method='xml')
          #output = description.text;
          return output
        
        except:
          print('exception raised')
          app.notfound();
          return;
    
    app.notfound();





# Return metadata by name from common metadata
class get_resource_id_specific_metadata_by_name:
  def GET(self, resource_id, metadata_name):
    print('get_resource_id_specific_metadata_by_name')
    print("getting resourceID="+str(resource_id)+" metadata="+str(metadata_name)+'content_type='+str(http_content_type))
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        resource = child;
        common_metadata   = resource.find('CommonMetadata');
        specific_metadata = resource.find('SpecificMetadata');

        resource_type = str(common_metadata.find('Type').text).strip();

        # Resource specific metadata to restrict search in case of redundant
        # tag/element names
        resource_specific_metadata = specific_metadata.find(resource_type);

        print('resource_specific_metadata='+str(ET.tostring(resource_specific_metadata, 'utf-8', method='xml')));

        if resource_type == resource_hypermodel:
            print("switch case\n") ;

        elif resource_type == resource_hypermodel:
            print("switch case\n"+resource_hypermodel) ;
        elif resource_type == resource_dataset:
            print("switch case\n"+resource_dataset) ;

        print('resource_type='+resource_type)

        try:
          xml_element = resource_specific_metadata.find(metadata_name);
          output = ET.tostring(xml_element, 'utf-8', method='xml')
          print('output='+str(output))

          if http_content_type != 'xml':
            output == xml_element.text

            #description = common_meta_data.find('Description');
            #output = ET.tostring(description, 'utf-8', method='xml')
            #output = description.text;
          return output

        except:
          print('exception raised')
          app.notfound();
          return;

    app.notfound();




# Return metadata by name from common metadata
class get_resource_id_common_metadata_by_name:
  def GET(self, resource_id, metadata_name):
    web.header('Content-Type', 'text/xml');
    print('get_resource_id_common_metadata_by_name');
    print("getting resourceID="+str(resource_id)+" metadata="+str(metadata_name)+'content_type='+str(http_content_type))
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        resource = child;
        common_metadata = resource.find('CommonMetadata');
        xml_element = common_metadata.find(metadata_name);

        try:
          output = ET.tostring(xml_element, 'utf-8', method='xml')
          print('output='+str(output))
          if http_content_type != 'xml':
            output == xml_element.text;
 
            #description = common_meta_data.find('Description');
            #output = ET.tostring(description, 'utf-8', method='xml')
            #output = description.text;
          return output
        except:
          print('exception raised')
          app.notfound();
        return;
  
    app.notfound();


# Return XML Element given resource_id and element name
class get_element_by_name:
  def GET(self, resource_id, element_name):
    web.header('Content-Type', 'text/xml');
    print('get_element_by_name');
    print("get resource description "+str(resource_id))
    # ET.dump(tree)
    #output = ET.tostring(root, 'utf-8', method='xml')
    
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        resource = child;
        xml_element = resource.find(element_name);
        #output = ET.tostring(child, 'utf-8', method='xml')
        #description = common_meta_data.find('Description');
        #output = ET.tostring(description, 'utf-8', method='xml')
        #output = description.text;
        return xml_element
  
    app.notfound();




# Return description for resource_id
class get_description:
  def GET(self, resource_id):
    print('get_description');
    print("get resource description "+str(resource_id))
    # ET.dump(tree)
    #output = ET.tostring(root, 'utf-8', method='xml')

    ct = web.ctx.env.get('CONTENT_TYPE')
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        resource = child;
        common_meta_data = resource.find('CommonMetadata');
        #output = ET.tostring(child, 'utf-8', method='xml')
        description = common_meta_data.find('Description');
        #output = ET.tostring(description, 'utf-8', method='xml')
        output = description.text;
        return output

    app.notfound();



# Return the XML for the resource with resource_id
class get_resource_xml:
  def GET(self, resource_id):
    web.header('Content-Type', 'text/xml')
    print('get_resource_xml');
    print("get resource "+str(resource_id))
    # ET.dump(tree)
    #output = ET.tostring(root, 'utf-8', method='xml')
    #return output
    for child in root:
      if child.attrib['resourceid'] == str(resource_id):
        output = ET.tostring(child, 'utf-8', method='xml')
        web.header('Content-Type', 'text/xml')
        #return render.response(output);
        return output
  
    app.notfound();

'''
class get_resource:
  def GET(self, resource_id):
    print "get resource"+'resource_id'
    # ET.dump(tree)
    #output = ET.tostring(root, 'utf-8', method='xml')
    #return output
    for child in root:
      #print str(child.attrib['resourceid'])
      if child.attrib['resourceid'] == str(resource_id):
        output = ET.tostring(child, 'utf-8', method='xml')
        return output
        #return str(child.attrib)
      else:
        app.notfound();
'''

'''
  TODO
  class get_model:
  def GET(self, model_id):
    models_root = tree.find('Resource')
    output = 'models:[';
    for child in models_root:
      print 'child', child.tag, child.attrib
      output += str(child.attrib) + str(child.text) +','
    outp  ut += ']';
    
    # TODO remove
    output += strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    return output
'''

class get_model_list:
    def GET(self):
        models_root = tree.find('Resource')
        output = 'models:[';
        for child in models_root:
            print('child', child.tag, child.attrib)
            output += str(child.attrib) + str(child.text) +','
        output += ']';
        
        # TODO remove
        output += strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        return output


#########################################################
class list_users:
    def GET(self):
        output = 'users:[';
        for child in root:
            print('child', child.tag, child.attrib)
            output += str(child.attrib) + ','
        output += ']';
        return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)
if __name__ == "__main__":
    app.run()

