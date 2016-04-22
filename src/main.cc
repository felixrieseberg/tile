#include "nan.h"
using namespace v8;

#include "tile.h"

namespace {

NAN_METHOD(Send) {
  Nan::HandleScope scope;
  bool success = tile::Send();
  info.GetReturnValue().Set(Nan::New<Boolean>(success));
}

void Init(Handle<Object> exports) {
  Nan::SetMethod(exports, "send", Send);
}

}  // namespace

NODE_MODULE(tile, Init)
