/**
 * Copyright 2019 Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef CONTRIB_PARSER_GRAMMAR_H_
#define CONTRIB_PARSER_GRAMMAR_H_

#include "./ast.h"
#include "./token.h"

namespace akg {
namespace ir {
class ASTStmtList;

ASTStmtList GenAST(TokState &stat);
}  // namespace ir
}  // namespace akg

#endif  // CONTRIB_PARSER_GRAMMAR_H_
