#JAVA_PARSER_Complier_Project

import yacc
import sys, os
from lexer import lexer,tokens

################################################################################

def p_start(p):
    '''start : CompilationUnit '''


def p_Modifier(p):
    ''' Modifier : Annotation
                 | PUBLIC
                 | PROTECTED
                 | PRIVATE
                 | ABSTRACT
                 | STATIC
                 | FINAL
                 | STRICTFP
                 | TRANSIENT
                 | VOLATILE
                 | SYNCHRONIZED
                 | NATIVE
                 | DEFAULT'''

def p_ModifierList(p):
    ''' ModifierList : Modifier ModifierList
                     | empty'''

# TODO: Support FOR unicode needs to be added
def p_Identifier(p):
    '''Identifier : IDENTIFIER'''

# TODO: Support FOR unicode needs to be added
#  JavaLetterOrDigit:
#  any Unicode character that is a "Java letter-or-digit"
#  def p_JavaLetterOrDigit(p):
    #  '''JavaLetterOrDigit :  '''

def p_Literal(p):
    '''Literal : DECIMALINT
               | DECIMALFLOATINGLIT
               | BOOLEANLIT
               | CHARLIT
               | STRINGLIT
               | NULLLIT'''

################################################################################

def p_Type(p):
    '''Type : PrimitiveType
            | ReferenceType'''


def p_PrimitiveType(p):
    '''PrimitiveType : MultAnnotation NumericType
                     | MultAnnotation BOOLEAN'''

def p_NumericType(p):
    '''NumericType : IntegralType
                     | FloatingPointType'''

def p_IntegralType(p):
    '''IntegralType : BYTE
                    | SHORT
                    | INT
                    | LONG
                    | CHAR'''

def p_FloatingPointType(p):
    '''FloatingPointType : FLOAT
                         | DOUBLE'''

def p_ReferenceType(p):
    '''ReferenceType : ClassOrInterfaceType
                     | ArrayType'''


def p_ClassOrInterfaceType(p):
    '''ClassOrInterfaceType : ClassType'''


def p_ClassType(p):
    '''ClassType : ClassOrInterfaceType DOT MultAnnotation Identifier TypeArguments
                 | ClassOrInterfaceType DOT MultAnnotation Identifier
                 | MultAnnotation Identifier TypeArguments
                 | MultAnnotation Identifier
                 '''

def p_MultAnnotation(p):
    '''MultAnnotation : Annotation MultAnnotation
                      | empty'''

def p_ArrayType(p):
    '''ArrayType : PrimitiveType Dims
                 | ClassOrInterfaceType Dims'''

def p_Dims(p):
    '''Dims : MultAnnotation LBRACKETS RBRACKETS Dims
            | MultAnnotation LBRACKETS RBRACKETS'''

def p_TypeParameter(p):
    '''TypeParameter : MultAnnotation Identifier TypeBound
                     | MultAnnotation Identifier'''


def p_TypeBound(p):
    '''TypeBound : EXTENDS ClassOrInterfaceType 
                 | EXTENDS ClassOrInterfaceType MultAdditionalBound
                 '''

def p_MultAdditionalBound(p):
  ''' MultAdditionalBound : MultAdditionalBound AdditionalBound
                          | AdditionalBound '''

def p_AdditionalBound(p):
    '''AdditionalBound : BOOLEANAND ClassType'''

def p_TypeArguments(p):
    '''TypeArguments : LESSTHAN TypeArgumentList GREATERTHAN'''

def p_TypeArgumentList(p):
    '''TypeArgumentList : TypeArgument COMMA TypeArgumentList
                        | TypeArgument'''

def p_TypeArgument(p):
    '''TypeArgument : ReferenceType
                    | Wildcard'''

def p_Wildcard(p):
    '''Wildcard : MultAnnotation QUESTIONMARK WildcardBounds
                | MultAnnotation QUESTIONMARK'''

def p_WildcardBounds(p):
    '''WildcardBounds : EXTENDS ReferenceType
                      | SUPER ReferenceType'''

################################################################################

def p_TypeName(p):
    '''TypeName : Identifier DOT TypeName
                | Identifier '''

################################################################################

#Removing Empty Program in Java
def p_CompilationUnit(p):
    '''CompilationUnit : PackageDeclaration MultImportDeclaration MultTypeDeclaration
                       | PackageDeclaration MultImportDeclaration
                       | PackageDeclaration MultTypeDeclaration
                       | MultImportDeclaration MultTypeDeclaration
                       | MultTypeDeclaration
                       | PackageDeclaration
                       | MultImportDeclaration
                       '''

def p_MultImportDeclaration(p):
    '''MultImportDeclaration : ImportDeclaration MultImportDeclaration
                             | ImportDeclaration'''

def p_MultTypeDeclaration(p):
    '''MultTypeDeclaration : TypeDeclaration MultTypeDeclaration
                           | TypeDeclaration'''

def p_PackageDeclaration(p):
    '''PackageDeclaration : MultAnnotation PACKAGE TypeName SEMICOLON'''

def p_ImportDeclaration(p):
    '''ImportDeclaration : SingleTypeImportDeclaration
                         | TypeImportOnDemandDeclaration
                         | SingleStaticImportDeclaration
                         | StaticImportOnDemandDeclaration '''

def p_SingleTypeImportDeclaration(p):
    '''SingleTypeImportDeclaration : IMPORT TypeName SEMICOLON '''


def p_TypeImportOnDemandDeclaration(p):
    '''TypeImportOnDemandDeclaration : IMPORT TypeName DOT MULTIPLY SEMICOLON'''

def p_SingleStaticImportDeclaration(p):
    '''SingleStaticImportDeclaration : IMPORT STATIC TypeName DOT Identifier SEMICOLON '''

def p_StaticImportOnDemandDeclaration(p):
    '''StaticImportOnDemandDeclaration :  IMPORT STATIC TypeName DOT MULTIPLY SEMICOLON'''

def p_TypeDeclaration(p):
    '''TypeDeclaration : ClassDeclaration
                       | InterfaceDeclaration
                       | SEMICOLON'''

################################################################################

def p_ClassDeclaration(p):
    '''ClassDeclaration : NormalClassDeclaration
                        | EnumDeclaration'''

def p_NormalClassDeclaration(p):
    '''NormalClassDeclaration : ModifierList CLASS Identifier TypeParameters Superclass Superinterfaces ClassBody
                              | ModifierList CLASS Identifier TypeParameters Superclass ClassBody
                              | ModifierList CLASS Identifier TypeParameters Superinterfaces ClassBody
                              | ModifierList CLASS Identifier Superclass Superinterfaces ClassBody
                              | ModifierList CLASS Identifier TypeParameters ClassBody
                              | ModifierList CLASS Identifier Superclass ClassBody
                              | ModifierList CLASS Identifier Superinterfaces ClassBody
                              | ModifierList CLASS Identifier ClassBody'''

def p_TypeParameters(p):
    '''TypeParameters : LESSTHAN TypeParameterList GREATERTHAN'''


def p_TypeParameterList(p):
    '''TypeParameterList : TypeParameter COMMA TypeParameterList
                         | TypeParameter'''

def p_Superclass(p):
    '''Superclass : EXTENDS ClassType'''


def p_Superinterfaces(p):
    '''Superinterfaces : IMPLEMENTS InterfaceTypeList '''

def p_InterfaceTypeList(p):
    '''InterfaceTypeList : ClassType COMMA InterfaceTypeList
                         | ClassType'''

def p_ClassBody(p):
    '''ClassBody : LBRACES MultClassBodyDeclaration RBRACES
                 | LBRACES RBRACES'''

def p_MultClassBodyDeclaration(p):
    '''MultClassBodyDeclaration : ClassBodyDeclaration MultClassBodyDeclaration
                                | ClassBodyDeclaration'''

def p_ClassBodyDeclaration(p):
    '''ClassBodyDeclaration : ClassMemberDeclaration
                            | InstanceInitializer
                            | StaticInitializer
                            | ConstructorDeclaration'''

def p_ClassMemberDeclaration(p):
    '''ClassMemberDeclaration : FieldDeclaration
                              | MethodDeclaration
                              | ClassDeclaration
                              | InterfaceDeclaration
                              | SEMICOLON '''

def p_FieldDeclaration(p):
    '''FieldDeclaration : ModifierList Type VariableDeclaratorList SEMICOLON'''


def p_VariableDeclaratorList(p):
    '''VariableDeclaratorList : VariableDeclarator COMMA VariableDeclaratorList
                              | VariableDeclarator '''

def p_VariableDeclarator(p):
    '''VariableDeclarator : VariableDeclaratorId EQUAL VariableInitializer
                          | VariableDeclaratorId'''

def p_VariableDeclaratorId(p):
    '''VariableDeclaratorId : Identifier Dims
                            | Identifier'''

def p_VariableInitializer(p):
    '''VariableInitializer : Expression
                           | ArrayInitializer '''


def p_MethodDeclaration(p):
    '''MethodDeclaration : ModifierList MethodHeader MethodBody'''


def p_MethodHeader(p):
    '''MethodHeader : Result MethodDeclarator Throws
                    | Result MethodDeclarator
                    | TypeParameters MultAnnotation Result MethodDeclarator Throws
                    | TypeParameters MultAnnotation Result MethodDeclarator
                    '''

def p_Result(p):
    '''Result : Type
              | VOID'''

def p_MethodDeclarator(p):
    '''MethodDeclarator : Identifier LPAREN FormalParameterList RPAREN Dims
                        | Identifier LPAREN FormalParameterList RPAREN
                        | Identifier LPAREN RPAREN Dims
                        | Identifier LPAREN RPAREN'''

def p_FormalParameterList(p):
    '''FormalParameterList : ReceiverParameter
                           | FormalParameters COMMA LastFormalParameter
                           | LastFormalParameter '''

def p_FormalParameters(p):
    '''FormalParameters : FormalParameter1
                        | FormalParameter2 '''

def p_FormalParameter1(p):
    '''FormalParameter1 : FormalParameter FormalParameter1
                        | FormalParameter'''

def p_FormalParameter2(p):
    '''FormalParameter2 : ReceiverParameter FormalParameter2
                        | ReceiverParameter'''
def p_FormalParameter(p):
    '''FormalParameter : ModifierList Type VariableDeclaratorId'''

def p_LastFormalParameter(p):
    '''LastFormalParameter : ModifierList Type MultAnnotation ELLIPSIS VariableDeclaratorId
                           | FormalParameter '''
def p_ReceiverParameter(p):
    '''ReceiverParameter : MultAnnotation Type Identifier DOT THIS
                         | MultAnnotation Type THIS'''


def p_Throws(p):
    '''Throws : THROWS ExceptionTypeList'''

def p_ExceptionTypeList(p):
    '''ExceptionTypeList : ExceptionType COMMA ExceptionTypeList
                         | ExceptionType '''

def p_ExceptionType(p):
    '''ExceptionType :  ClassType'''


def p_MethodBody(p):
    '''MethodBody : Block
                  | SEMICOLON'''

def p_InstanceInitializer(p):
    '''InstanceInitializer :  Block'''


def p_StaticInitializer(p):
    '''StaticInitializer : STATIC Block'''


def p_ConstructorDeclaration(p):
    '''ConstructorDeclaration : ModifierList ConstructorDeclarator Throws ConstructorBody'''

def p_ConstructorModifier(p):
    '''ConstructorModifier : Annotation
                           | PUBLIC
                           | PROTECTED
                           | PRIVATE '''

def p_ConstructorDeclarator(p):
    '''ConstructorDeclarator : TypeParameters SimpleTypeName LPAREN FormalParameterList RPAREN
                             | TypeParameters SimpleTypeName LPAREN RPAREN
                             | SimpleTypeName LPAREN FormalParameterList RPAREN
                             | SimpleTypeName LPAREN RPAREN '''
def p_SimpleTypeName(p):
    '''SimpleTypeName : Identifier '''


def p_ConstructorBody(p):
    '''ConstructorBody : LBRACES ExplicitConstructorInvocation BlockStatements RBRACES
                       | LBRACES ExplicitConstructorInvocation RBRACES
                       | LBRACES BlockStatements RBRACES
                       | LBRACES RBRACES '''

def p_ExplicitConstructorInvocation(p):
    '''ExplicitConstructorInvocation : TypeArguments THIS LPAREN ArgumentList RPAREN SEMICOLON
                                     | TypeArguments THIS LPAREN RPAREN SEMICOLON
                                     | THIS LPAREN ArgumentList RPAREN SEMICOLON
                                     | THIS LPAREN RPAREN SEMICOLON
                                     | TypeArguments SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | TypeArguments SUPER LPAREN RPAREN SEMICOLON
                                     | SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | SUPER LPAREN RPAREN SEMICOLON
                                     | TypeName DOT TypeArguments SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | TypeName DOT TypeArguments SUPER LPAREN RPAREN SEMICOLON
                                     | TypeName DOT SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | TypeName DOT SUPER LPAREN RPAREN SEMICOLON
                                     | Primary DOT TypeArguments SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | Primary DOT TypeArguments SUPER LPAREN RPAREN SEMICOLON
                                     | Primary DOT SUPER LPAREN ArgumentList RPAREN SEMICOLON
                                     | Primary DOT SUPER LPAREN RPAREN SEMICOLON '''

def p_EnumDeclaration(p):
    '''EnumDeclaration : ModifierList ENUM Identifier Superinterfaces EnumBody
                       | ModifierList ENUM Identifier EnumBody'''

def p_EnumBody(p):
    '''EnumBody : LBRACES EnumConstantList COMMA EnumBodyDeclarations RBRACES
                | LBRACES EnumConstantList COMMA RBRACES
                | LBRACES EnumConstantList EnumBodyDeclarations RBRACES
                | LBRACES COMMA EnumBodyDeclarations RBRACES
                | LBRACES EnumBodyDeclarations RBRACES
                | LBRACES EnumConstantList RBRACES
                | LBRACES COMMA RBRACES
                | LBRACES RBRACES '''

def p_EnumConstantList(p):
    '''EnumConstantList : EnumConstant COMMA EnumConstantList
                        | EnumConstant'''

def p_EnumConstant(p):
    '''EnumConstant : MultEnumConstantModifier Identifier LPAREN ArgumentList RPAREN ClassBody
                    | MultEnumConstantModifier Identifier LPAREN ArgumentList RPAREN
                    | MultEnumConstantModifier Identifier LPAREN RPAREN ClassBody
                    | Identifier LPAREN ArgumentList RPAREN ClassBody
                    | Identifier LPAREN RPAREN ClassBody
                    | Identifier LPAREN ArgumentList RPAREN
                    | MultEnumConstantModifier Identifier LPAREN RPAREN
                    | Identifier LPAREN RPAREN
                    | MultEnumConstantModifier Identifier ClassBody
                    | MultEnumConstantModifier Identifier
                    | Identifier ClassBody
                    | Identifier '''

def p_MultEnumConstantModifier(p):
    '''MultEnumConstantModifier : EnumConstantModifier MultEnumConstantModifier
                                | EnumConstantModifier'''

def p_EnumConstantModifier(p):
    '''EnumConstantModifier : Annotation'''

def p_EnumBodyDeclarations(p):
    '''EnumBodyDeclarations : SEMICOLON MultClassBodyDeclaration
                            | SEMICOLON '''

def p_InterfaceDeclaration(p):
    '''InterfaceDeclaration : NormalInterfaceDeclaration
                            | AnnotationTypeDeclaration'''

def p_NormalInterfaceDeclaration(p):
    '''NormalInterfaceDeclaration : ModifierList INTERFACE Identifier TypeParameters ExtendsInterfaces InterfaceBody
                                  | ModifierList INTERFACE Identifier ExtendsInterfaces InterfaceBody
                                  | ModifierList INTERFACE Identifier TypeParameters InterfaceBody
                                  | ModifierList INTERFACE Identifier InterfaceBody'''


def p_ExtendsInterfaces(p):
    '''ExtendsInterfaces : EXTENDS InterfaceTypeList '''

def p_InterfaceBody(p):
    '''InterfaceBody : LBRACES MultInterfaceMemberDeclaration RBRACES
                     | LBRACES RBRACES'''

def p_InterfaceMemberDeclaration(p):
    '''InterfaceMemberDeclaration : ConstantDeclaration
                                  | InterfaceMethodDeclaration
                                  | ClassDeclaration
                                  | InterfaceDeclaration
                                  | SEMICOLON'''

def p_MultInterfaceMemberDeclaration(p):
    '''MultInterfaceMemberDeclaration : InterfaceMemberDeclaration MultInterfaceMemberDeclaration
                                      | InterfaceMemberDeclaration'''


def p_ConstantDeclaration(p):
    '''ConstantDeclaration : ModifierList Type VariableDeclaratorList SEMICOLON'''

def p_InterfaceMethodDeclaration(p):
    '''InterfaceMethodDeclaration : ModifierList MethodHeader MethodBody'''

def p_AnnotationTypeDeclaration(p):
    '''AnnotationTypeDeclaration : ModifierList AT INTERFACE Identifier AnnotationTypeBody'''

def p_AnnotationTypeBody(p):
    '''AnnotationTypeBody : LBRACES MultAnnotationTypeMemberDeclaration RBRACES
                          | LBRACES RBRACES'''

def p_MultAnnotationTypeMemberDeclaration(p):
    '''MultAnnotationTypeMemberDeclaration : AnnotationTypeMemberDeclaration MultAnnotationTypeMemberDeclaration
                                           | AnnotationTypeMemberDeclaration'''

def p_AnnotationTypeMemberDeclaration(p):
    '''AnnotationTypeMemberDeclaration : AnnotationTypeElementDeclaration
                                       | ConstantDeclaration
                                       | ClassDeclaration
                                       | InterfaceDeclaration
                                       | SEMICOLON '''

def p_AnnotationTypeElementDeclaration(p):
    '''AnnotationTypeElementDeclaration : MultAnnotationTypeElementModifier Type Identifier LPAREN RPAREN Dims DefaultValue SEMICOLON
                                        | Type Identifier LPAREN RPAREN Dims DefaultValue SEMICOLON
                                        | MultAnnotationTypeElementModifier Type Identifier LPAREN RPAREN DefaultValue SEMICOLON
                                        | MultAnnotationTypeElementModifier Type Identifier LPAREN RPAREN Dims SEMICOLON
                                        | MultAnnotationTypeElementModifier Type Identifier LPAREN RPAREN SEMICOLON
                                        | Type Identifier LPAREN RPAREN DefaultValue SEMICOLON
                                        | Type Identifier LPAREN RPAREN Dims SEMICOLON
                                        | Type Identifier LPAREN RPAREN SEMICOLON '''


def p_MultAnnotationTypeElementModifier(p):
    '''MultAnnotationTypeElementModifier : AnnotationTypeElementModifier MultAnnotationTypeElementModifier
                      | AnnotationTypeElementModifier'''

def p_AnnotationTypeElementModifier(p):
    '''AnnotationTypeElementModifier : AnnotationTypeElementModifier1
                                     | AnnotationTypeElementModifier2'''

def p_AnnotationTypeElementModifier1(p):
    '''AnnotationTypeElementModifier1 : Annotation
                                      | PUBLIC'''

def p_AnnotationTypeElementModifier2(p):
    '''AnnotationTypeElementModifier2 : ABSTRACT'''

def p_DefaultValue(p):
    '''DefaultValue :  DEFAULT ElementValue'''

def p_Annotation(p):
    '''Annotation : NormalAnnotation
                  | MarkerAnnotation
                  | SingleElementAnnotation'''

def p_NormalAnnotation(p):
    '''NormalAnnotation : AT TypeName LPAREN ElementValuePairList RPAREN '''

def p_ElementValuePairList(p):
    '''ElementValuePairList : ElementValuePairList COMMA ElementValuePair
                            | ElementValuePair
                            | empty '''

def p_ElementValuePair(p):
    '''ElementValuePair : Identifier EQUAL ElementValue'''

def p_ElementValue(p):
    '''ElementValue : ConditionalExpression
                    | ElementValueArrayInitializer
                    | Annotation '''

def p_ElementValueArrayInitializer(p):
    '''ElementValueArrayInitializer : LBRACES ElementValueList COMMA RBRACES
                                    | LBRACES ElementValueList RBRACES
                                    | LBRACES COMMA RBRACES
                                    | LBRACES RBRACES '''

def p_ElementValueList(p):
    '''ElementValueList : ElementValue COMMA ElementValueList
                        | ElementValue'''

def p_MarkerAnnotation(p):
    '''MarkerAnnotation : AT TypeName '''

def p_SingleElementAnnotation(p):
    '''SingleElementAnnotation :  AT TypeName LPAREN ElementValue RPAREN'''

################################################################################

def p_ArrayInitializer(p):
    '''ArrayInitializer : LBRACES VariableInitializerList COMMA RBRACES
                        | LBRACES VariableInitializerList RBRACES
                        | LBRACES COMMA RBRACES
                        | LBRACES RBRACES
                        '''


def p_VariableInitializerList(p):
    '''VariableInitializerList : VariableInitializer COMMA VariableInitializerList
                               | VariableInitializer'''

################################################################################

def p_Block(p):
    '''Block : LBRACES BlockStatements RBRACES
             | LBRACES RBRACES '''

def p_BlockStatements(p):
    '''BlockStatements : MultBlockStatement'''

def p_MultBlockStatement(p):
    '''MultBlockStatement : BlockStatement MultBlockStatement
                      | BlockStatement'''

def p_BlockStatement(p):
    '''BlockStatement : LocalVariableDeclarationStatement
                      | ClassDeclaration
                      | Statement'''

def p_LocalVariableDeclarationStatement(p):
    '''LocalVariableDeclarationStatement : LocalVariableDeclaration SEMICOLON '''

def p_LocalVariableDeclaration(p):
    '''LocalVariableDeclaration : ModifierList Type VariableDeclaratorList'''

def p_Statement(p):
    '''Statement : StatementWithoutTrailingSubstatement
                 | LabeledStatement
                 | IfThenStatement
                 | IfThenElseStatement
                 | WhileStatement
                 | ForStatement'''

def p_StatementNoShortIf(p):
    '''StatementNoShortIf : StatementWithoutTrailingSubstatement
                          | LabeledStatementNoShortIf
                          | IfThenElseStatementNoShortIf
                          | WhileStatementNoShortIf
                          | ForStatementNoShortIf'''

def p_StatementWithoutTrailingSubstatement(p):
    '''StatementWithoutTrailingSubstatement : Block
                                            | EmptyStatement
                                            | ExpressionStatement
                                            | AssertStatement
                                            | SwitchStatement
                                            | DoStatement
                                            | BreakStatement
                                            | ContinueStatement
                                            | ReturnStatement
                                            | SynchronizedStatement
                                            | ThrowStatement
                                            | TryStatement'''

def p_EmptyStatement(p):
    '''EmptyStatement : SEMICOLON'''

def p_LabeledStatement(p):
    '''LabeledStatement : Identifier COLON Statement '''

def p_LabeledStatementNoShortIf(p):
    '''LabeledStatementNoShortIf : Identifier COLON StatementNoShortIf '''

def p_ExpressionStatement(p):
    '''ExpressionStatement : StatementExpression SEMICOLON '''

def p_StatementExpression(p):
    '''StatementExpression : Assignment
                           | PreIncrementExpression
                           | PreDecrementExpression
                           | PostIncrementExpression
                           | PostDecrementExpression
                           | MethodInvocation
                           | ClassInstanceCreationExpression'''

def p_IfThenStatement(p):
    '''IfThenStatement :  IF LPAREN Expression RPAREN Statement'''
    '''IfThenStatement :  IF LPAREN Expression RPAREN Statement'''

def p_IfThenElseStatement(p):
    '''IfThenElseStatement : IF LPAREN Expression RPAREN StatementNoShortIf ELSE Statement '''

def p_IfThenElseStatementNoShortIf(p):
    '''IfThenElseStatementNoShortIf : IF LPAREN Expression RPAREN StatementNoShortIf ELSE StatementNoShortIf '''


def p_AssertStatement(p):
    '''AssertStatement : ASSERT Expression SEMICOLON
                       | ASSERT Expression COLON Expression SEMICOLON'''

def p_SwitchStatement(p):
    '''SwitchStatement : SWITCH LPAREN Expression RPAREN SwitchBlock '''

def p_SwitchBlock(p):
    '''SwitchBlock : LBRACES MultSwitchBlockStatementGroup MultSwitchLabel RBRACES
                   | LBRACES MultSwitchBlockStatementGroup RBRACES
                   | LBRACES MultSwitchLabel RBRACES
                   | LBRACES RBRACES '''


def p_MultSwitchBlockStatementGroup(p):
    '''MultSwitchBlockStatementGroup : SwitchBlockStatementGroup MultSwitchBlockStatementGroup
                      | SwitchBlockStatementGroup'''

def p_SwitchBlockStatementGroup(p):
    '''SwitchBlockStatementGroup :  MultSwitchLabel BlockStatements'''


def p_MultSwitchLabel(p):
    '''MultSwitchLabel : SwitchLabel MultSwitchLabel
                       | SwitchLabel'''

def p_SwitchLabel(p):
    '''SwitchLabel : CASE ConstantExpression COLON
                   | CASE Identifier COLON
                   | DEFAULT COLON'''

def p_WhileStatement(p):
    '''WhileStatement : WHILE LPAREN Expression RPAREN Statement '''

def p_WhileStatementNoShortIf(p):
    '''WhileStatementNoShortIf :  WHILE LPAREN Expression RPAREN StatementNoShortIf'''

def p_DoStatement(p):
    '''DoStatement :  DO Statement WHILE LPAREN Expression RPAREN SEMICOLON'''

def p_ForStatement(p):
    '''ForStatement : BasicForStatement
                    | EnhancedForStatement'''

def p_ForStatementNoShortIf(p):
    '''ForStatementNoShortIf : BasicForStatementNoShortIf
                             | EnhancedForStatementNoShortIf '''

def p_BasicForStatement(p):
    '''BasicForStatement : FOR LPAREN ForInit SEMICOLON Expression SEMICOLON ForUpdate RPAREN Statement
                         | FOR LPAREN ForInit SEMICOLON Expression SEMICOLON RPAREN Statement
                         | FOR LPAREN ForInit SEMICOLON SEMICOLON ForUpdate RPAREN Statement
                         | FOR LPAREN SEMICOLON Expression SEMICOLON ForUpdate RPAREN Statement
                         | FOR LPAREN SEMICOLON SEMICOLON ForUpdate RPAREN Statement
                         | FOR LPAREN SEMICOLON Expression SEMICOLON RPAREN Statement
                         | FOR LPAREN ForInit SEMICOLON SEMICOLON RPAREN Statement
                         | FOR LPAREN SEMICOLON SEMICOLON RPAREN Statement
                         '''

def p_BasicForStatementNoShortIf(p):
    '''BasicForStatementNoShortIf : FOR LPAREN ForInit SEMICOLON Expression SEMICOLON ForUpdate RPAREN StatementNoShortIf
                                  | FOR LPAREN ForInit SEMICOLON Expression SEMICOLON RPAREN StatementNoShortIf
                                  | FOR LPAREN ForInit SEMICOLON SEMICOLON ForUpdate RPAREN StatementNoShortIf
                                  | FOR LPAREN SEMICOLON Expression SEMICOLON ForUpdate RPAREN StatementNoShortIf
                                  | FOR LPAREN SEMICOLON SEMICOLON ForUpdate RPAREN StatementNoShortIf
                                  | FOR LPAREN SEMICOLON Expression SEMICOLON RPAREN StatementNoShortIf
                                  | FOR LPAREN ForInit SEMICOLON SEMICOLON RPAREN StatementNoShortIf
                                  | FOR LPAREN SEMICOLON SEMICOLON RPAREN StatementNoShortIf'''

def p_ForInit(p):
    '''ForInit : StatementExpressionList
               | LocalVariableDeclaration'''

def p_ForUpdate(p):
    '''ForUpdate : StatementExpressionList'''

def p_StatementExpressionList(p):
    '''StatementExpressionList : StatementExpression COMMA StatementExpressionList
                               | StatementExpression'''

def p_EnhancedForStatement(p):
    '''EnhancedForStatement : FOR LPAREN ModifierList Type VariableDeclaratorId COLON Expression RPAREN Statement'''


def p_EnhancedForStatementNoShortIf(p):
    '''EnhancedForStatementNoShortIf : FOR LPAREN ModifierList Type VariableDeclaratorId COLON Expression RPAREN StatementNoShortIf'''

def p_BreakStatement(p):
    '''BreakStatement : BREAK Identifier SEMICOLON
                      | BREAK SEMICOLON'''

def p_ContinueStatement(p):
    '''ContinueStatement : CONTINUE Identifier SEMICOLON
                         | CONTINUE SEMICOLON '''

def p_ReturnStatement(p):
    '''ReturnStatement : RETURN Expression SEMICOLON
                       | RETURN SEMICOLON'''

def p_ThrowStatement(p):
    '''ThrowStatement : THROW Expression SEMICOLON '''

def p_SynchronizedStatement(p):
    '''SynchronizedStatement : SYNCHRONIZED LPAREN Expression RPAREN Block '''

def p_TryStatement(p):
    '''TryStatement : TRY Block Catches Finally
                    | TRY Block Catches
                    | TRY Block Finally
                    | TryWithResourcesStatement '''

def p_Catches(p):
    '''Catches : MultCatchClause'''

def p_MultCatchClause(p):
    '''MultCatchClause : CatchClause MultCatchClause
                       | CatchClause'''

def p_CatchClause(p):
    '''CatchClause : CATCH LPAREN CatchFormalParameter RPAREN Block '''

def p_CatchFormalParameter(p):
    '''CatchFormalParameter : ModifierList CatchType VariableDeclaratorId'''

def p_CatchType(p):
    '''CatchType : ClassType BOOLEANOR MultCatchType1
                 | ClassType '''

def p_MultCatchType1(p):
    '''MultCatchType1 : BOOLEANOR CatchType MultCatchType1
                     | empty'''

def p_Finally(p):
    '''Finally : FINALLY Block '''

def p_TryWithResourcesStatement(p):
    '''TryWithResourcesStatement : TRY ResourceSpecification Block Catches Finally
                                 | TRY ResourceSpecification Block Catches
                                 | TRY ResourceSpecification Block Finally
                                 | TRY ResourceSpecification Block '''

def p_ResourceSpecification(p):
    '''ResourceSpecification : LPAREN ResourceList SEMICOLON RPAREN
                             | LPAREN ResourceList RPAREN '''

def p_ResourceList(p):
    '''ResourceList : Resource SEMICOLON ResourceList
                    | Resource'''

def p_Resource(p):
    '''Resource : ModifierList Type VariableDeclaratorId EQUAL Expression'''

################################################################################

def p_Primary(p):
    '''Primary : PrimaryNoNewArray
               | ArrayCreationExpression '''

def p_PrimaryNoNewArray(p):
    '''PrimaryNoNewArray : Literal
                         | ClassLiteral
                         | THIS
                         | TypeName DOT THIS
                         | LPAREN Expression RPAREN
                         | ClassInstanceCreationExpression
                         | FieldAccess
                         | ArrayAccess
                         | MethodInvocation
                         | MethodReference'''

def p_ClassLiteral(p):
    '''ClassLiteral : TypeName Brackets DOT CLASS
                    | NumericType Brackets DOT CLASS
                    | BOOLEAN Brackets DOT CLASS
                    | VOID DOT CLASS'''

def p_ClassInstanceCreationExpression(p):
    '''ClassInstanceCreationExpression : UnqualifiedClassInstanceCreationExpression
                                       | TypeName DOT UnqualifiedClassInstanceCreationExpression
                                       | Primary DOT UnqualifiedClassInstanceCreationExpression'''

def p_UnqualifiedClassInstanceCreationExpression(p):
    '''UnqualifiedClassInstanceCreationExpression : NEW TypeArguments ClassOrInterfaceTypeToInstantiate LPAREN ArgumentList RPAREN ClassBody
                                                  | NEW ClassOrInterfaceTypeToInstantiate LPAREN ArgumentList RPAREN ClassBody
                                                  | NEW TypeArguments ClassOrInterfaceTypeToInstantiate LPAREN RPAREN ClassBody
                                                  | NEW TypeArguments ClassOrInterfaceTypeToInstantiate LPAREN ArgumentList RPAREN
                                                  | NEW TypeArguments ClassOrInterfaceTypeToInstantiate LPAREN RPAREN
                                                  | NEW ClassOrInterfaceTypeToInstantiate LPAREN ArgumentList RPAREN
                                                  | NEW ClassOrInterfaceTypeToInstantiate LPAREN RPAREN ClassBody
                                                  | NEW ClassOrInterfaceTypeToInstantiate LPAREN RPAREN '''

def p_ClassOrInterfaceTypeToInstantiate(p):
    '''ClassOrInterfaceTypeToInstantiate : MultAnnotation Identifier ClassOrInterfaceTypeToInstantiate1 TypeArgumentsOrDiamond
                                         | MultAnnotation Identifier TypeArgumentsOrDiamond
                                         | MultAnnotation Identifier ClassOrInterfaceTypeToInstantiate1
                                         | MultAnnotation Identifier'''

def p_ClassOrInterfaceTypeToInstantiate1(p):
    '''ClassOrInterfaceTypeToInstantiate1 : DOT MultAnnotation Identifier ClassOrInterfaceTypeToInstantiate1
                                          | empty '''

def p_TypeArgumentsOrDiamond(p):
    '''TypeArgumentsOrDiamond : TypeArguments
                              | LESSTHAN GREATERTHAN'''

def p_FieldAccess(p):
    '''FieldAccess : Primary DOT Identifier
                   | SUPER DOT Identifier
                   | TypeName DOT SUPER DOT Identifier'''

def p_ArrayAccess(p):
    '''ArrayAccess : TypeName LBRACKETS Expression RBRACKETS
                   | PrimaryNoNewArray LBRACKETS Expression RBRACKETS '''

def p_MethodInvocation(p):
    '''MethodInvocation : Identifier LPAREN ArgumentList RPAREN
                        | Identifier LPAREN RPAREN
                        | TypeName DOT TypeArguments Identifier LPAREN ArgumentList RPAREN
                        | TypeName DOT Identifier LPAREN ArgumentList RPAREN
                        | TypeName DOT TypeArguments Identifier LPAREN RPAREN
                        | TypeName DOT Identifier LPAREN RPAREN
                        | Primary DOT TypeArguments Identifier LPAREN ArgumentList RPAREN
                        | Primary DOT Identifier LPAREN ArgumentList RPAREN
                        | Primary DOT TypeArguments Identifier LPAREN RPAREN
                        | Primary DOT Identifier LPAREN RPAREN
                        | SUPER DOT TypeArguments Identifier LPAREN ArgumentList RPAREN
                        | SUPER DOT Identifier LPAREN ArgumentList RPAREN
                        | SUPER DOT TypeArguments Identifier LPAREN RPAREN
                        | SUPER DOT Identifier LPAREN RPAREN
                        | TypeName DOT SUPER DOT TypeArguments Identifier LPAREN ArgumentList RPAREN
                        | TypeName DOT SUPER DOT Identifier LPAREN ArgumentList RPAREN
                        | TypeName DOT SUPER DOT TypeArguments Identifier LPAREN RPAREN
                        | TypeName DOT SUPER DOT Identifier LPAREN RPAREN '''

def p_ArgumentList(p):
    '''ArgumentList : Expression COMMA ArgumentList
                    | Expression'''

def p_MethodReference(p):
    '''MethodReference : TypeName DOUBLECOLON TypeArguments Identifier
                       | TypeName DOUBLECOLON Identifier
                       | ReferenceType DOUBLECOLON TypeArguments Identifier
                       | ReferenceType DOUBLECOLON Identifier
                       | Primary DOUBLECOLON TypeArguments Identifier
                       | Primary DOUBLECOLON Identifier
                       | SUPER DOUBLECOLON TypeArguments Identifier
                       | SUPER DOUBLECOLON Identifier
                       | TypeName DOT SUPER DOUBLECOLON TypeArguments Identifier
                       | TypeName DOT SUPER DOUBLECOLON Identifier
                       | ClassType DOUBLECOLON TypeArguments NEW
                       | ClassType DOUBLECOLON NEW
                       | ArrayType DOUBLECOLON NEW '''

def p_ArrayCreationExpression(p):
    '''ArrayCreationExpression : NEW PrimitiveType DimExprs Dims
                               | NEW PrimitiveType DimExprs
                               | NEW ClassOrInterfaceType DimExprs Dims
                               | NEW ClassOrInterfaceType DimExprs
                               | NEW PrimitiveType Dims ArrayInitializer
                               | NEW ClassOrInterfaceType Dims ArrayInitializer'''

def p_DimExprs(p):
    '''DimExprs : DimExpr DimExprs
                | DimExpr'''

def p_DimExpr(p):
    '''DimExpr : MultAnnotation LBRACKETS Expression RBRACKETS'''

def p_Expression(p):
    '''Expression : LambdaExpression
                  | AssignmentExpression '''

def p_LambdaExpression(p):
    '''LambdaExpression : LambdaParameters ARROW LambdaBody '''

def p_LambdaParameters(p):
    '''LambdaParameters : Identifier
                        | LPAREN FormalParameterList RPAREN
                        | LPAREN RPAREN
                        | LPAREN InferredFormalParameterList RPAREN '''


def p_InferredFormalParameterList(p):
    '''InferredFormalParameterList : Identifier COMMA InferredFormalParameterList
                                   | Identifier'''


def p_LambdaBody(p):
    '''LambdaBody : Expression
                  | Block '''

def p_AssignmentExpression(p):
    '''AssignmentExpression : ConditionalExpression
                            | Assignment '''

def p_Assignment(p):
    '''Assignment : LeftHandSide AssignmentOperator Expression'''

def p_LeftHandSide(p):
    '''LeftHandSide : TypeName
                    | FieldAccess
                    | ArrayAccess '''

def p_AssignmentOperator(p):
    '''AssignmentOperator : EQUAL
                          | MULTIPLYEQUALS
                          | DIVIDEEQUALS
                          | MODULOEQUALS
                          | PLUSEQUALS
                          | MINUSEQUALS
                          | LEFTSHIFTEQUALS
                          | RIGHTSHIFTEQUALS
                          | URIGHTSHIFTEQUALS
                          | ANDEQUALS
                          | XOREQUALS
                          | OREQUALS'''

def p_ConditionalExpression(p):
    '''ConditionalExpression : ConditionalOrExpression
                             | ConditionalOrExpression QUESTIONMARK Expression COLON ConditionalExpression
                             | ConditionalOrExpression QUESTIONMARK Expression COLON LambdaExpression'''


def p_ConditionalOrExpression(p):
    '''ConditionalOrExpression : ConditionalAndExpression
                               | ConditionalOrExpression OR ConditionalAndExpression '''


def p_ConditionalAndExpression(p):
    '''ConditionalAndExpression : InclusiveOrExpression
                                | ConditionalAndExpression AND InclusiveOrExpression'''

def p_InclusiveOrExpression(p):
    '''InclusiveOrExpression : ExclusiveOrExpression
                             | InclusiveOrExpression BOOLEANOR ExclusiveOrExpression'''


def p_ExclusiveOrExpression(p):
    '''ExclusiveOrExpression : AndExpression
                             | ExclusiveOrExpression BOOLEANXOR AndExpression '''


def p_AndExpression(p):
    '''AndExpression : EqualityExpression
                     | AndExpression BOOLEANAND EqualityExpression '''


def p_EqualityExpression(p):
    '''EqualityExpression : RelationalExpression
                          | EqualityExpression EQUALS RelationalExpression
                          | EqualityExpression NOTEQUALS RelationalExpression '''


def p_RelationalExpression(p):
    '''RelationalExpression : ShiftExpression
                            | RelationalExpression LESSTHAN ShiftExpression
                            | RelationalExpression GREATERTHAN ShiftExpression
                            | RelationalExpression LESSTHANEQUAL ShiftExpression
                            | RelationalExpression GREATERTHANEQUAL ShiftExpression
                            | RelationalExpression INSTANCEOF ReferenceType'''


def p_ShiftExpression(p):
    '''ShiftExpression : AdditiveExpression
                       | ShiftExpression LEFTSHIFT AdditiveExpression
                       | ShiftExpression RIGHTSHIFT AdditiveExpression
                       | ShiftExpression URIGHTSHIFT AdditiveExpression '''

#Removed left recursion
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression AdditiveExpression_dash '''

def p_AdditiveExpression_dash(p):
    '''AdditiveExpression_dash : PLUS MultiplicativeExpression AdditiveExpression_dash
                               | MINUS MultiplicativeExpression AdditiveExpression_dash
                               | empty'''

def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : UnaryExpression MultiplicativeExpression_dash '''

def p_MultiplicativeExpression_dash(p):
    '''MultiplicativeExpression_dash : MULTIPLY UnaryExpression MultiplicativeExpression_dash
                                     | DIVIDE UnaryExpression MultiplicativeExpression_dash
                                     | MODULO UnaryExpression MultiplicativeExpression_dash
                                     | empty'''

def p_UnaryExpression(p):
    '''UnaryExpression : PreIncrementExpression
                       | PreDecrementExpression
                       | PLUS UnaryExpression
                       | MINUS UnaryExpression
                       | UnaryExpressionNotPlusMinus '''

def p_PreIncrementExpression(p):
    '''PreIncrementExpression : PLUSPLUS UnaryExpression '''

def p_PreDecrementExpression(p):
    '''PreDecrementExpression : MINUSMINUS UnaryExpression '''


def p_UnaryExpressionNotPlusMinus(p):
    '''UnaryExpressionNotPlusMinus : PostfixExpression
                                   | TILDA UnaryExpression
                                   | BOOLEANNOT UnaryExpression
                                   | CastExpression '''

def p_PostfixExpression(p):
    '''PostfixExpression : Primary
                         | TypeName
                         | PostIncrementExpression
                         | PostDecrementExpression'''

def p_PostIncrementExpression(p):
    '''PostIncrementExpression : PostfixExpression PLUSPLUS'''

def p_PostDecrementExpression(p):
    '''PostDecrementExpression : PostfixExpression MINUSMINUS'''

def p_CastExpression(p):
    '''CastExpression : LPAREN PrimitiveType RPAREN UnaryExpression
                      | LPAREN ReferenceType MultAdditionalBound RPAREN UnaryExpressionNotPlusMinus
                      | LPAREN ReferenceType RPAREN UnaryExpressionNotPlusMinus
                      | LPAREN ReferenceType MultAdditionalBound RPAREN LambdaExpression
                      | LPAREN ReferenceType RPAREN LambdaExpression '''


def p_ConstantExpression(p):
    '''ConstantExpression : Expression '''

################################################################################

#Default Error
def p_error(p):
    print("Input Error: ", p)
    return

#Empty_Production
def p_empty(p):
     'empty :'
     pass 

def p_Brackets(p):
	''' Brackets : LBRACKETS RBRACKETS Brackets
                     | empty'''

# Build the parser
if __name__ == '__main__':
    parser = yacc.yacc()

    file=open(sys.argv[1],'r')
    test=file.read()

    file_path = sys.argv[1]
    if (not os.path.isfile(file_path)):
        print("The file doesn't exist. EXITING.")
        sys.exit(-1)

    file1 = open(file_path)
    code = file1.read()

    parser.parse(code,lexer, True, True)

