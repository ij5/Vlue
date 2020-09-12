<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:d3967559-3fd8-4459-a41b-07a4e9393dc0(Vlue.editor)">
  <persistence version="9" />
  <languages>
    <use id="18bc6592-03a6-4e29-a83a-7ff23bde13ba" name="jetbrains.mps.lang.editor" version="14" />
    <devkit ref="fbc25dd2-5da4-483a-8b19-70928e1b62d7(jetbrains.mps.devkit.general-purpose)" />
  </languages>
  <imports>
    <import index="pcc5" ref="r:dbcbf018-9e33-40a8-b1ee-a4a799dd46a2(Vlue.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="18bc6592-03a6-4e29-a83a-7ff23bde13ba" name="jetbrains.mps.lang.editor">
      <concept id="1071666914219" name="jetbrains.mps.lang.editor.structure.ConceptEditorDeclaration" flags="ig" index="24kQdi" />
      <concept id="1237303669825" name="jetbrains.mps.lang.editor.structure.CellLayout_Indent" flags="nn" index="l2Vlx" />
      <concept id="1080736578640" name="jetbrains.mps.lang.editor.structure.BaseEditorComponent" flags="ig" index="2wURMF">
        <child id="1080736633877" name="cellModel" index="2wV5jI" />
      </concept>
      <concept id="1073389446423" name="jetbrains.mps.lang.editor.structure.CellModel_Collection" flags="sn" stub="3013115976261988961" index="3EZMnI">
        <child id="1106270802874" name="cellLayout" index="2iSdaV" />
        <child id="1073389446424" name="childCellModel" index="3EZMnx" />
      </concept>
      <concept id="1073389577006" name="jetbrains.mps.lang.editor.structure.CellModel_Constant" flags="sn" stub="3610246225209162225" index="3F0ifn">
        <property id="1073389577007" name="text" index="3F0ifm" />
      </concept>
      <concept id="1166049232041" name="jetbrains.mps.lang.editor.structure.AbstractComponent" flags="ng" index="1XWOmA">
        <reference id="1166049300910" name="conceptDeclaration" index="1XX52x" />
      </concept>
    </language>
  </registry>
  <node concept="24kQdi" id="64uTfoZShOj">
    <ref role="1XX52x" to="pcc5:64uTfoZShOg" resolve="Calculator" />
    <node concept="3EZMnI" id="64uTfoZShPD" role="2wV5jI">
      <node concept="3F0ifn" id="64uTfoZShPK" role="3EZMnx">
        <property role="3F0ifm" value="calculator" />
      </node>
      <node concept="3F0ifn" id="64uTfoZShQ2" role="3EZMnx">
        <property role="3F0ifm" value="{name}" />
      </node>
      <node concept="l2Vlx" id="64uTfoZShPG" role="2iSdaV" />
    </node>
  </node>
</model>

