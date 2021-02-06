import QtQuick 2.10
import QtQuick.Controls 2.1
import QtQuick.Window 2.2

ApplicationWindow {
    id: applicationWindow
    title: qsTr("Covid Dashboard")
    width: 640
    height: 480
    visible: true
    color: "#333333"

    Button {
        id: button
        text: qsTr("Click Me")
        anchors.verticalCenter: parent.verticalCenter
        autoExclusive: true
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
