#!/usr/bin/python3

# Copyright 2021 AIR Institute
# See LICENSE for details.

from flask_restx import fields

from smartclide_dle.api.v1 import api


bpmn_example = """
<?xml version="1.0" encoding="UTF-8"?>
<!-- origin at X=0.0 Y=0.0 -->
<bpmn2:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmn20="http://www.omg.org/bpmn20" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:bpsim="http://www.bpsim.org/schemas/1.0" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:drools="http://www.jboss.org/drools" xmlns="http://www.jboss.org/drools" xmlns:ns="http://www.w3.org/2001/XMLSchema" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd http://www.jboss.org/drools drools.xsd http://www.bpsim.org/schemas/1.0 bpsim.xsd" id="_Ij6tsItIEemS2vwQqZKIHQ" exporter="org.eclipse.bpmn2.modeler.core" exporterVersion="1.5.0.Final-v20180515-1642-B1" targetNamespace="http://www.omg.org/bpmn20">
  <bpmn2:itemDefinition id="_idItem" isCollection="false" structureRef="java.lang.Long"/>
  <bpmn2:itemDefinition id="_taskNameItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_processNameItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_isApprovedItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_stateOfCorrespondenceItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_domainItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_transactionIdItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_ws_process_rest_urlItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_BusinessAdministratorIdProcessItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="_actorDetailItem" isCollection="false" structureRef="com.intrasoft.process.domain.common.ActorDTO"/>
  <bpmn2:itemDefinition id="__0EE798C4-B9B0-4EBB-B27A-380548B0E41F_ContainerIdInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__0EE798C4-B9B0-4EBB-B27A-380548B0E41F_topicInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__0EE798C4-B9B0-4EBB-B27A-380548B0E41F_idInputXItem" isCollection="false" structureRef="java.lang.Long"/>
  <bpmn2:itemDefinition id="__0EE798C4-B9B0-4EBB-B27A-380548B0E41F_transactionIdInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__0EE798C4-B9B0-4EBB-B27A-380548B0E41F_ResultOutputXItem" isCollection="false" structureRef="java.lang.Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_PriorityInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_CommentInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_DescriptionInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_CreatedByInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_GroupIdInputXItem" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputXItem" isCollection="false" structureRef="java.lang.Long"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_jobInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_ContainerIdInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_topicInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_idInputXItem" isCollection="false" structureRef="java.lang.Long"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_stateOfCorrespondenceInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_transactionIdInputXItem" isCollection="false" structureRef="String"/>
  <bpmn2:itemDefinition id="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_ResultOutputXItem" isCollection="false" structureRef="java.lang.Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_1" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_2" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_3" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_4" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_5" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_6" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_7" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_8" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_9" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_10" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_11" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_12" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_13" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_14" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_15" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_16" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_17" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_18" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_19" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_20" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_21" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_22" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_23" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_24" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_25" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_26" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_27" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_28" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_29" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_30" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_31" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_32" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_33" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_34" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_35" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_36" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_37" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_38" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_39" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_40" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_41" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_42" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_43" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_44" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_45" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_46" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_47" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_48" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_49" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_50" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_51" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_52" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_53" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_54" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_55" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_56" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_57" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_58" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_59" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_60" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_61" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_62" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_63" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_64" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_65" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_66" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_67" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_68" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_69" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_70" isCollection="false" structureRef="Object"/>
  <bpmn2:itemDefinition id="ItemDefinition_71" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_72" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_73" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_74" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_75" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_76" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_77" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_78" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_79" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_80" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_81" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_82" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_83" isCollection="false"/>
  <bpmn2:itemDefinition id="ItemDefinition_84" isCollection="false"/>
  <bpmn2:signal id="Signal_1" name="WaitingForAppealResultsSignal"/>
  <bpmn2:process id="Benefits.MedicalCommitteeResults" drools:packageName="com.myspace.benefits" drools:version="1.0" drools:adHoc="false" name="MedicalCommitteeResults" isExecutable="true">
    <bpmn2:property id="id" itemSubjectRef="_idItem" name="id"/>
    <bpmn2:property id="taskName" itemSubjectRef="_taskNameItem" name="taskName"/>
    <bpmn2:property id="processName" itemSubjectRef="_processNameItem" name="processName"/>
    <bpmn2:property id="isApproved" itemSubjectRef="_isApprovedItem" name="isApproved"/>
    <bpmn2:property id="correspondenceState" itemSubjectRef="_stateOfCorrespondenceItem" name="correspondenceState"/>
    <bpmn2:property id="domain" itemSubjectRef="_domainItem" name="domain"/>
    <bpmn2:property id="transactionId" itemSubjectRef="_transactionIdItem" name="transactionId"/>
    <bpmn2:property id="ws_process_rest_url" itemSubjectRef="_ws_process_rest_urlItem" name="ws_process_rest_url"/>
    <bpmn2:property id="actorDetail" itemSubjectRef="_actorDetailItem" name="actorDetail"/>
    <bpmn2:property id="organizationUnit" itemSubjectRef="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_idInputXItem" name="organizationUnit"/>
    <bpmn2:property id="returnedByHigherLevel" itemSubjectRef="__3989005F-BD00-4FD5-B9B1-2851F5D83D76_transactionIdInputXItem" name="returnedByHigherLevel"/>
    <bpmn2:sequenceFlow id="_B3C92F4F-6B6A-4610-994E-CD4A92608A37" sourceRef="_46BE84F1-DF57-40DD-B96B-0E0117828DD2" targetRef="Task_1">
      <bpmn2:extensionElements>
        <drools:metaData name="isAutoConnection.target">
          <drools:metaValue><![CDATA[true]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
    </bpmn2:sequenceFlow>
    <bpmn2:sequenceFlow id="_1DC3B732-FC11-4A70-BC20-B8AD180EAA4E" sourceRef="_63A0CEB6-7D97-48D7-9D95-86576ED761BE" targetRef="Task_2"/>
    <bpmn2:startEvent id="_63A0CEB6-7D97-48D7-9D95-86576ED761BE" name="Medical Committee Results">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Medical Committee Results]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:outgoing>_1DC3B732-FC11-4A70-BC20-B8AD180EAA4E</bpmn2:outgoing>
    </bpmn2:startEvent>
    <bpmn2:userTask id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2" name="Handle Medical Committee Results">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Handle Medical Committee Results]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:incoming>SequenceFlow_2</bpmn2:incoming>
      <bpmn2:outgoing>_B3C92F4F-6B6A-4610-994E-CD4A92608A37</bpmn2:outgoing>
      <bpmn2:ioSpecification id="_Ij7UzotIEemS2vwQqZKIHQ">
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputX" drools:dtype="Object" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputXItem" name="TaskName"/>
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputX" drools:dtype="java.lang.Long" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputXItem" name="id"/>
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputX" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputXItem" name="isApproved"/>
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputX" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputXItem" name="correspondenceState"/>
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputX" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputXItem" name="BusinessAdministratorId"/>
        <bpmn2:dataInput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputX" drools:dtype="Object" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputXItem" name="Skippable"/>
        <bpmn2:dataOutput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputX" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputXItem" name="isApproved"/>
        <bpmn2:dataOutput id="_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputX" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputXItem" name="correspondenceState"/>
        <bpmn2:inputSet id="_Ij7Uz4tIEemS2vwQqZKIHQ">
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputX</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputX</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputX</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputX</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputX</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputX</bpmn2:dataInputRefs>
        </bpmn2:inputSet>
        <bpmn2:outputSet id="_Ij7U0ItIEemS2vwQqZKIHQ">
          <bpmn2:dataOutputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputX</bpmn2:dataOutputRefs>
          <bpmn2:dataOutputRefs>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputX</bpmn2:dataOutputRefs>
        </bpmn2:outputSet>
      </bpmn2:ioSpecification>
      <bpmn2:dataInputAssociation id="_Ij7U0YtIEemS2vwQqZKIHQ">
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputX</bpmn2:targetRef>
        <bpmn2:assignment id="_Ij7U0otIEemS2vwQqZKIHQ">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="_Ij7U04tIEemS2vwQqZKIHQ"><![CDATA[Task]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="_Ij7U1ItIEemS2vwQqZKIHQ">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="_Ij7U1YtIEemS2vwQqZKIHQ">
        <bpmn2:sourceRef>id</bpmn2:sourceRef>
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputX</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="_Ij7U1otIEemS2vwQqZKIHQ">
        <bpmn2:sourceRef>isApproved</bpmn2:sourceRef>
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputX</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="_Ij7U14tIEemS2vwQqZKIHQ">
        <bpmn2:sourceRef>correspondenceState</bpmn2:sourceRef>
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputX</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="_Ij7U3ItIEemS2vwQqZKIHQ">
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputX</bpmn2:targetRef>
        <bpmn2:assignment id="_Ij7U3YtIEemS2vwQqZKIHQ">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="_Ij7U3otIEemS2vwQqZKIHQ"><![CDATA[#{actorDetail.businessOwnerNames}]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="_Ij7U34tIEemS2vwQqZKIHQ">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="_Ij7U4ItIEemS2vwQqZKIHQ">
        <bpmn2:targetRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputX</bpmn2:targetRef>
        <bpmn2:assignment id="_Ij7U4YtIEemS2vwQqZKIHQ">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="_Ij7U4otIEemS2vwQqZKIHQ"><![CDATA[false]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="_Ij7U44tIEemS2vwQqZKIHQ">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataOutputAssociation id="_Ij7U5ItIEemS2vwQqZKIHQ">
        <bpmn2:sourceRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputX</bpmn2:sourceRef>
        <bpmn2:targetRef>isApproved</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
      <bpmn2:dataOutputAssociation id="_Ij7U5YtIEemS2vwQqZKIHQ">
        <bpmn2:sourceRef>_46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputX</bpmn2:sourceRef>
        <bpmn2:targetRef>correspondenceState</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
      <bpmn2:potentialOwner id="PotentialOwner_1" name="Potential Owner 1">
        <bpmn2:resourceAssignmentExpression id="ResourceAssignmentExpression_1">
          <bpmn2:formalExpression id="FormalExpression_1">#{actorDetail.actors}</bpmn2:formalExpression>
        </bpmn2:resourceAssignmentExpression>
      </bpmn2:potentialOwner>
    </bpmn2:userTask>
    <bpmn2:task id="Task_1" drools:taskName="Rest" name="Task Assignment">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Task Assignment]]></drools:metaValue>
        </drools:metaData>
        <drools:metaData name="customAsync">
          <drools:metaValue><![CDATA[true]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:incoming>_B3C92F4F-6B6A-4610-994E-CD4A92608A37</bpmn2:incoming>
      <bpmn2:outgoing>SequenceFlow_1</bpmn2:outgoing>
      <bpmn2:ioSpecification id="InputOutputSpecification_1">
        <bpmn2:dataInput id="DataInput_15" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_UrlInputXItem" name="Url"/>
        <bpmn2:dataInput id="DataInput_16" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_UsernameInputXItem" name="Username"/>
        <bpmn2:dataInput id="DataInput_17" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ConnectTimeoutInputXItem" name="ConnectTimeout"/>
        <bpmn2:dataInput id="DataInput_18" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ContentDataInputXItem" name="ContentData"/>
        <bpmn2:dataInput id="DataInput_19" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_MethodInputXItem" name="Method"/>
        <bpmn2:dataInput id="DataInput_20" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_PasswordInputXItem" name="Password"/>
        <bpmn2:dataInput id="DataInput_21" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ReadTimeoutInputXItem" name="ReadTimeout"/>
        <bpmn2:dataInput id="DataInput_22" drools:dtype="" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="HandleResponseErrors"/>
        <bpmn2:dataInput id="DataInput_23" drools:dtype="" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="ResultClass"/>
        <bpmn2:dataInput id="DataInput_24" drools:dtype="Object" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="TaskName"/>
        <bpmn2:dataOutput id="DataOutput_1" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ResultOutputXItem" name="Result"/>
        <bpmn2:inputSet id="InputSet_1">
          <bpmn2:dataInputRefs>DataInput_15</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_16</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_17</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_18</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_19</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_20</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_21</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_22</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_23</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_24</bpmn2:dataInputRefs>
        </bpmn2:inputSet>
        <bpmn2:outputSet id="OutputSet_1">
          <bpmn2:dataOutputRefs>DataOutput_1</bpmn2:dataOutputRefs>
        </bpmn2:outputSet>
      </bpmn2:ioSpecification>
      <bpmn2:dataInputAssociation id="DataInputAssociation_1">
        <bpmn2:targetRef>DataInput_15</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_1">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_2">#{ws_process_rest_url}/ssp.webservices.process/rs/task/task/findActors?taskName=ReviewMedicalCommitteeResults&amp;processName=Benefits.MedicalCommitteeResults</bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_3">_31F01606-436E-466D-B7DC-0C2F0C1C2322_UrlInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_2">
        <bpmn2:targetRef>DataInput_22</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_2">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_4"><![CDATA[true]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_5">_31F01606-436E-466D-B7DC-0C2F0C1C2322_HandleResponseErrorsInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_3">
        <bpmn2:targetRef>DataInput_23</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_3">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_6"><![CDATA[com.intrasoft.process.domain.common.ActorDTO]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_7">_31F01606-436E-466D-B7DC-0C2F0C1C2322_ResultClassInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_4">
        <bpmn2:targetRef>DataInput_24</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_4">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_8"><![CDATA[Rest]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_9">_31F01606-436E-466D-B7DC-0C2F0C1C2322_TaskNameInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataOutputAssociation id="DataOutputAssociation_1">
        <bpmn2:sourceRef>DataOutput_1</bpmn2:sourceRef>
        <bpmn2:targetRef>actorDetail</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
    </bpmn2:task>
    <bpmn2:userTask id="UserTask_1" name="Review Medical Committee Results">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Review Medical Committee Results]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:incoming>SequenceFlow_1</bpmn2:incoming>
      <bpmn2:outgoing>SequenceFlow_3</bpmn2:outgoing>
      <bpmn2:ioSpecification id="InputOutputSpecification_2">
        <bpmn2:dataInput id="DataInput_25" drools:dtype="Object" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputXItem" name="TaskName"/>
        <bpmn2:dataInput id="DataInput_26" drools:dtype="java.lang.Long" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_CorrespondenceIdInputXItem" name="id"/>
        <bpmn2:dataInput id="DataInput_27" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedInputXItem" name="isApproved"/>
        <bpmn2:dataInput id="DataInput_28" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceInputXItem" name="correspondenceState"/>
        <bpmn2:dataInput id="DataInput_30" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputXItem" name="BusinessAdministratorId"/>
        <bpmn2:dataInput id="DataInput_31" drools:dtype="Object" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputXItem" name="Skippable"/>
        <bpmn2:dataOutput id="DataOutput_2" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_isApprovedOutputXItem" name="isApproved"/>
        <bpmn2:dataOutput id="DataOutput_3" drools:dtype="String" itemSubjectRef="__46BE84F1-DF57-40DD-B96B-0E0117828DD2_stateOfCorrespondenceOutputXItem" name="correspondenceState"/>
        <bpmn2:inputSet id="InputSet_2">
          <bpmn2:dataInputRefs>DataInput_25</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_26</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_27</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_28</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_30</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_31</bpmn2:dataInputRefs>
        </bpmn2:inputSet>
        <bpmn2:outputSet id="OutputSet_2">
          <bpmn2:dataOutputRefs>DataOutput_2</bpmn2:dataOutputRefs>
          <bpmn2:dataOutputRefs>DataOutput_3</bpmn2:dataOutputRefs>
        </bpmn2:outputSet>
      </bpmn2:ioSpecification>
      <bpmn2:dataInputAssociation id="DataInputAssociation_5">
        <bpmn2:targetRef>DataInput_25</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_5">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_10"><![CDATA[Task]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_11">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_TaskNameInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_6">
        <bpmn2:sourceRef>id</bpmn2:sourceRef>
        <bpmn2:targetRef>DataInput_26</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_7">
        <bpmn2:sourceRef>isApproved</bpmn2:sourceRef>
        <bpmn2:targetRef>DataInput_27</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_8">
        <bpmn2:sourceRef>correspondenceState</bpmn2:sourceRef>
        <bpmn2:targetRef>DataInput_28</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_10">
        <bpmn2:targetRef>DataInput_30</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_7">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_14"><![CDATA[#{actorDetail.businessOwnerNames}]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_15">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_BusinessAdministratorIdInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_11">
        <bpmn2:targetRef>DataInput_31</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_8">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_16"><![CDATA[false]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_17">_46BE84F1-DF57-40DD-B96B-0E0117828DD2_SkippableInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataOutputAssociation id="DataOutputAssociation_2">
        <bpmn2:sourceRef>DataOutput_2</bpmn2:sourceRef>
        <bpmn2:targetRef>isApproved</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
      <bpmn2:dataOutputAssociation id="DataOutputAssociation_3">
        <bpmn2:sourceRef>DataOutput_3</bpmn2:sourceRef>
        <bpmn2:targetRef>correspondenceState</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
      <bpmn2:potentialOwner id="PotentialOwner_2" name="Potential Owner 1">
        <bpmn2:resourceAssignmentExpression id="ResourceAssignmentExpression_2">
          <bpmn2:formalExpression id="FormalExpression_18">#{actorDetail.actors}</bpmn2:formalExpression>
        </bpmn2:resourceAssignmentExpression>
      </bpmn2:potentialOwner>
    </bpmn2:userTask>
    <bpmn2:sequenceFlow id="SequenceFlow_1" drools:priority="1" sourceRef="Task_1" targetRef="UserTask_1"/>
    <bpmn2:endEvent id="EndEvent_1" name="Medical Committee Results Terminated">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Medical Committee Results Terminated]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:incoming>SequenceFlow_3</bpmn2:incoming>
      <bpmn2:dataInput id="DataInput_1" name="Signal_1_Input"/>
      <bpmn2:dataInputAssociation id="DataInputAssociation_12">
        <bpmn2:sourceRef>isApproved</bpmn2:sourceRef>
        <bpmn2:targetRef>DataInput_1</bpmn2:targetRef>
      </bpmn2:dataInputAssociation>
      <bpmn2:inputSet id="InputSet_3" name="Input Set 3">
        <bpmn2:dataInputRefs>DataInput_1</bpmn2:dataInputRefs>
      </bpmn2:inputSet>
      <bpmn2:signalEventDefinition id="SignalEventDefinition_1" signalRef="Signal_1"/>
    </bpmn2:endEvent>
    <bpmn2:sequenceFlow id="SequenceFlow_3" drools:priority="1" sourceRef="UserTask_1" targetRef="EndEvent_1"/>
    <bpmn2:task id="Task_2" drools:taskName="Rest" name="Task Assignment">
      <bpmn2:extensionElements>
        <drools:metaData name="elementname">
          <drools:metaValue><![CDATA[Task Assignment]]></drools:metaValue>
        </drools:metaData>
        <drools:metaData name="customAsync">
          <drools:metaValue><![CDATA[true]]></drools:metaValue>
        </drools:metaData>
      </bpmn2:extensionElements>
      <bpmn2:incoming>_1DC3B732-FC11-4A70-BC20-B8AD180EAA4E</bpmn2:incoming>
      <bpmn2:outgoing>SequenceFlow_2</bpmn2:outgoing>
      <bpmn2:ioSpecification id="InputOutputSpecification_3">
        <bpmn2:dataInput id="DataInput_33" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_UrlInputXItem" name="Url"/>
        <bpmn2:dataInput id="DataInput_34" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_UsernameInputXItem" name="Username"/>
        <bpmn2:dataInput id="DataInput_35" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ConnectTimeoutInputXItem" name="ConnectTimeout"/>
        <bpmn2:dataInput id="DataInput_36" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ContentDataInputXItem" name="ContentData"/>
        <bpmn2:dataInput id="DataInput_37" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_MethodInputXItem" name="Method"/>
        <bpmn2:dataInput id="DataInput_38" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_PasswordInputXItem" name="Password"/>
        <bpmn2:dataInput id="DataInput_39" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ReadTimeoutInputXItem" name="ReadTimeout"/>
        <bpmn2:dataInput id="DataInput_40" drools:dtype="" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="HandleResponseErrors"/>
        <bpmn2:dataInput id="DataInput_41" drools:dtype="" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="ResultClass"/>
        <bpmn2:dataInput id="DataInput_42" drools:dtype="Object" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__91826CCF-11A6-410B-B7FD-0D51A7C3A448_ReadTimeoutInputXItem" name="TaskName"/>
        <bpmn2:dataOutput id="DataOutput_4" drools:dtype="String" itemSubjectRef="C.29%20-%20Old%20Age%20Pension.bpmn#__31F01606-436E-466D-B7DC-0C2F0C1C2322_ResultOutputXItem" name="Result"/>
        <bpmn2:inputSet id="InputSet_4">
          <bpmn2:dataInputRefs>DataInput_33</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_34</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_35</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_36</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_37</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_38</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_39</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_40</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_41</bpmn2:dataInputRefs>
          <bpmn2:dataInputRefs>DataInput_42</bpmn2:dataInputRefs>
        </bpmn2:inputSet>
        <bpmn2:outputSet id="OutputSet_3">
          <bpmn2:dataOutputRefs>DataOutput_4</bpmn2:dataOutputRefs>
        </bpmn2:outputSet>
      </bpmn2:ioSpecification>
      <bpmn2:dataInputAssociation id="DataInputAssociation_13">
        <bpmn2:targetRef>DataInput_33</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_9">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_19">#{ws_process_rest_url}/ssp.webservices.process/rs/task/task/findActors?taskName=HandleMedicalCommitteeResults&amp;processName=Benefits.MedicalCommitteeResults</bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_20">_31F01606-436E-466D-B7DC-0C2F0C1C2322_UrlInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_14">
        <bpmn2:targetRef>DataInput_40</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_10">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_21"><![CDATA[true]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_22">_31F01606-436E-466D-B7DC-0C2F0C1C2322_HandleResponseErrorsInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_15">
        <bpmn2:targetRef>DataInput_41</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_11">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_23"><![CDATA[com.intrasoft.process.domain.common.ActorDTO]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_24">_31F01606-436E-466D-B7DC-0C2F0C1C2322_ResultClassInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataInputAssociation id="DataInputAssociation_16">
        <bpmn2:targetRef>DataInput_42</bpmn2:targetRef>
        <bpmn2:assignment id="Assignment_12">
          <bpmn2:from xsi:type="bpmn2:tFormalExpression" id="FormalExpression_25"><![CDATA[Rest]]></bpmn2:from>
          <bpmn2:to xsi:type="bpmn2:tFormalExpression" id="FormalExpression_26">_31F01606-436E-466D-B7DC-0C2F0C1C2322_TaskNameInputX</bpmn2:to>
        </bpmn2:assignment>
      </bpmn2:dataInputAssociation>
      <bpmn2:dataOutputAssociation id="DataOutputAssociation_4">
        <bpmn2:sourceRef>DataOutput_4</bpmn2:sourceRef>
        <bpmn2:targetRef>actorDetail</bpmn2:targetRef>
      </bpmn2:dataOutputAssociation>
    </bpmn2:task>
    <bpmn2:sequenceFlow id="SequenceFlow_2" drools:priority="1" sourceRef="Task_2" targetRef="_46BE84F1-DF57-40DD-B96B-0E0117828DD2"/>
  </bpmn2:process>
  <bpmndi:BPMNDiagram id="_Ij7U-YtIEemS2vwQqZKIHQ">
    <bpmndi:BPMNPlane id="_Ij7U-otIEemS2vwQqZKIHQ" bpmnElement="Benefits.MedicalCommitteeResults">
      <bpmndi:BPMNShape id="shape__46BE84F1-DF57-40DD-B96B-0E0117828DD2" bpmnElement="_46BE84F1-DF57-40DD-B96B-0E0117828DD2">
        <dc:Bounds height="102.0" width="154.0" x="420.0" y="270.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_2">
          <dc:Bounds height="30.0" width="110.0" x="442.0" y="306.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape__63A0CEB6-7D97-48D7-9D95-86576ED761BE" bpmnElement="_63A0CEB6-7D97-48D7-9D95-86576ED761BE">
        <dc:Bounds height="56.0" width="56.0" x="100.0" y="100.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_4">
          <dc:Bounds height="45.0" width="67.0" x="95.0" y="156.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="BPMNShape_Task_1" bpmnElement="Task_1">
        <dc:Bounds height="102.0" width="154.0" x="660.0" y="270.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_1">
          <dc:Bounds height="15.0" width="96.0" x="689.0" y="313.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="BPMNShape_UserTask_1" bpmnElement="UserTask_1">
        <dc:Bounds height="102.0" width="154.0" x="900.0" y="270.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_3">
          <dc:Bounds height="30.0" width="110.0" x="922.0" y="306.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="BPMNShape_EndEvent_1" bpmnElement="EndEvent_1">
        <dc:Bounds height="36.0" width="36.0" x="1210.0" y="110.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_5">
          <dc:Bounds height="60.0" width="67.0" x="1195.0" y="146.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="BPMNShape_Task_2" bpmnElement="Task_2">
        <dc:Bounds height="102.0" width="154.0" x="190.0" y="270.0"/>
        <bpmndi:BPMNLabel>
          <dc:Bounds height="15.0" width="96.0" x="219.0" y="313.0"/>
        </bpmndi:BPMNLabel>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="edge_shape__63A0CEB6-7D97-48D7-9D95-86576ED761BE_to_shape__46BE84F1-DF57-40DD-B96B-0E0117828DD2" bpmnElement="_1DC3B732-FC11-4A70-BC20-B8AD180EAA4E" sourceElement="shape__63A0CEB6-7D97-48D7-9D95-86576ED761BE" targetElement="BPMNShape_Task_2">
        <di:waypoint xsi:type="dc:Point" x="128.0" y="156.0"/>
        <di:waypoint xsi:type="dc:Point" x="128.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="190.0" y="321.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_10"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge_shape__46BE84F1-DF57-40DD-B96B-0E0117828DD2_to_shape__3989005F-BD00-4FD5-B9B1-2851F5D83D76" bpmnElement="_B3C92F4F-6B6A-4610-994E-CD4A92608A37" sourceElement="shape__46BE84F1-DF57-40DD-B96B-0E0117828DD2" targetElement="BPMNShape_Task_1">
        <di:waypoint xsi:type="dc:Point" x="574.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="617.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="660.0" y="321.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_11"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="BPMNEdge_SequenceFlow_1" bpmnElement="SequenceFlow_1" sourceElement="BPMNShape_Task_1" targetElement="BPMNShape_UserTask_1">
        <di:waypoint xsi:type="dc:Point" x="814.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="857.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="900.0" y="321.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_5"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="BPMNEdge_SequenceFlow_3" bpmnElement="SequenceFlow_3" sourceElement="BPMNShape_UserTask_1" targetElement="BPMNShape_EndEvent_1">
        <di:waypoint xsi:type="dc:Point" x="1054.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="1228.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="1228.0" y="146.0"/>
        <bpmndi:BPMNLabel id="BPMNLabel_6"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="BPMNEdge_SequenceFlow_2" bpmnElement="SequenceFlow_2" sourceElement="BPMNShape_Task_2" targetElement="shape__46BE84F1-DF57-40DD-B96B-0E0117828DD2">
        <di:waypoint xsi:type="dc:Point" x="344.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="382.0" y="321.0"/>
        <di:waypoint xsi:type="dc:Point" x="420.0" y="321.0"/>
        <bpmndi:BPMNLabel/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn2:definitions>
"""

gherkin_example = """
Feature: Serve coffee
  In order to earn money
  Customers should be able to 
  buy coffee at all times

  Scenario: Buy last coffee
    Given there are 1 coffees left in the machine
    And I have deposited 1$
    When I press the coffee button
    Then I should be served a coffee
"""


_service_model = api.model('Service', {
    'id': fields.String(description="The service's id", required=True, example="_13BAF867-3CA8-4C6F-85C6-D3FD748D07D2"),
    'name': fields.String(description="The service's name", required=True, example="UserService")
}, description="The service specification")

_enviroment_prediction = api.model('RawEnviromentPrediction', {
    'user_volume': fields.Integer(description="The approximate number of user for what the enviroment must be deployed to", required=True, example=10),
    'space': fields.Integer(description="The service's required disk space (in Gb)", required=True, example=80),
    'memory': fields.Integer(description="The service's required memory (in Gb)", required=True, example=10)
}, description="The environment's own prediction")

enviroment_model = api.model('EnviromentPredictionRequest', {
    'header': fields.String(description="The prediction type identification", required=True, example="resource used"),
    'service': fields.Nested(_service_model, description="The service's information", required=True),
    'current_memory': fields.Integer(description="The service's current RAM value (in Gb)", required=True, example=8),
    'current_space': fields.Integer(description="The service's current disk value (in Gb)", required=True, example=256),
    'current_user_volume': fields.Integer(description="The service's current user volume value (in Gb)", required=True, example=4),
    'current_number_of_threads': fields.Integer(description="The service's current number of required threads value (in Gb)", required=True, example=2)
}, description="The enviroment reccomendation input request")

enviroment_prediction_model = api.model('EnviromentPrediction', {
    'header': fields.String(description="The prediction type identification", required=True, example="resource used"),
    'service': fields.Nested(_service_model, description="The service's information", required=True),
    'environments': fields.List(fields.Nested(_enviroment_prediction), description="The recommended service's enviroments for each user volume ranges", required=True)
}, description="The recommended environment for the service deployment")


acceptance_model = api.model('AcceptaceRequest', {
    'bpmn': fields.String(description="An XML formatted BPMN", required=True, example=bpmn_example),
}, description="The acceptance test reccomendation model input request")

acceptance_prediction_model = api.model('AcceptacePrediction', {
    'recommended_gherkins': fields.List(fields.String(example=gherkin_example), description="Gherkins recommended for the given BPMN", required=True),
}, description="The recommended gherkin for acceptance tests")


codegen_model = api.model('CodeGenRequest', {
    'code_input': fields.String(description="The code used as seed for the code generation", required=True, example='import android'),
    'method': fields.String(description="Method used to generate the code", required=True, example='advanced'),
    'language': fields.String(description="Language within the code generation is made", required=True, example='java'),
    'code_sugg_len': fields.Integer(description="Suggested length of the code generation", required=True, example=4),
    'code_sugg_lines': fields.Integer(description="Suggested lines that must have the generated code", required=True, example=2)
}, description="The code generation recommendation input request")

codegen_prediction_model = api.model('CodeGenPrediction', {
    'method': fields.String(description="Method used to generate the code", required=True, example='Default'),
    'language': fields.String(description="Language within the code generation is made", required=True, example='java'),
    'code_suggestions': fields.List(fields.String(example='support v4 view View'), description="Generated lins of code", required=True),
    'code_len': fields.Integer(description='Number of characters of generated code', example=10),
    'code_lines': fields.Integer(description='Number of lines of generated code', example=10)
}, description="The recommended gherkin for acceptance tests")


developer_model = api.model('DeveloperRequest', {
    'header': fields.String(description="The type of changes in repository", required=True, example="new commit"),
    'repo_id': fields.String(description="The id of the repository. The usual value is the URL.", required=True, example="https://github.com/example/example"),
    'state': fields.String(description="Status", required=True, example="info"),
    'user': fields.String(description="User's nickname in repository", required=True, example="mcdave"),
    'branch': fields.String(description="Repostory branch", required=True, example="dependabot/bundler/iloveruby/13-rails.5/rubyzip-1.3.0"),
    'time_since_last_commit': fields.Integer(description="Number of seconds since last commit", required=False, example=4),
    'number_of_files_modified': fields.Integer(description="Number of modified files since last commit", required=False, example=3),
}, description="The developer recommendation input request")

developer_prediction_model = api.model('DeveloperPrediction', {
    'header': fields.String(description="The type of changes in repository", required=True, example="new commit"),
    'repo_id': fields.String(description="The id of the repository. The usual value is the URL.", required=True, example="https://github.com/example/example"),
    'state': fields.String(description="Status", required=True, example="info"),
    'user': fields.String(description="User's nickname in repository", required=True, example="mcdave"),
    'conviction_to_commit_from_files': fields.Float(description="The percentage of users that would had commit on the current number of modified files.", required=False, example=0.1),
    'conviction_to_commit_from_time': fields.Float(description="The percentage of users that would had commit on the current time passed since last commit.", required=False, example=0.6)
}, description="The recommended action for the developer")


service_classification_model = api.model('ServiceClassificationRequest', {
    'service_id': fields.Integer(description="The id of the service to classify", required=True, example=34333),
    'service_name': fields.String(description="The name of the service to classify", required=True, example="TransLoc openAPI"),
    'service_desc': fields.String(description="The description of the service to classify", required=True, example="The TransLoc OpenAPI is a public RESTful API which allows developers to access real-time vehicle tracking information and incorporate this data into their website or mobile application.")
}, description="The service classification model recommendation input request")

service_classification_prediction_model = api.model('ServiceClassificationPrediction', {
    'service_id': fields.Integer(description="The id of the service to classify", required=True, example=34333),
    'service_name': fields.String(description="The name of the service to classify", required=True, example="TransLoc openAPI"),
    'service_class': fields.List(fields.String(example="Transportation"), description="The topic within the service has been classified", required=True),
    'method': fields.String(description="Method used to classify", required=True, example="Default"),
}, description="The method used to perform the clasification")


code_generation_templates_model = api.model('CodeGenerationRequest', {
    'bpmn_file': fields.String(description="File with the BPMN specification of the service creation", required=True, example=bpmn_example)
}, description="The template based code generation input request")

code_generation_templates_prediction_model = api.model('CodeGenerationResponse', {
    'code': fields.String(description="generated code in Java class", required=True)
}, description="The template based code generation output prediction")


bpmnitemrecommendation_model = api.model('BPMNRecommendationRequest', {
    'bpmn': fields.String(description="An XML formatted BPMN", required=True, example=bpmn_example),
}, description="The service test reccomendation model input request")

bpmnitemrecommendation_prediction_model = api.model('BPMNRecommendationPrediction', {
    'recommended_services': fields.List(fields.String(example="10"), description="ID's of reccomended services", required=True),
}, description="The recommended service's ids")
