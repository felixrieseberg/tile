#include "tile.h"

#include <windows.h>
#include <windows.ui.notifications.h>
#include <wrl/implements.h>

using namespace ABI::Windows::UI::Notifications; 
using namespace ABI::Windows::Data::Xml::Dom; 

namespace tile {

bool Send() {
  XmlDocument^ tileXml = TileUpdateManager::GetTemplateContent(TileTemplateType::TileSquareImage); 
  
  XmlNodeList^ tileImageAttributes = tileXml->GetElementsByTagName("image"); 
  //************************************************************************************* 
  // the static_cast or a dynamic_cast is used to move the image in to the element  
  // Item 0 or the first item 
  // in this case, you only get a single item, so you must use item 0, otherwise you get an 
  // error 
  dynamic_cast<XmlElement^>(tileImageAttributes->Item(0))->SetAttribute("src", "http://content.artofmanliness.com/uploads/2008/07/coral-snake.jpg");  
  TileNotification^ tileNotification = ref new TileNotification(tileXml); 
  TileUpdateManager::CreateTileUpdaterForApplication()->Update(tileNotification); 

  return true;
}

}  // namespace tile
