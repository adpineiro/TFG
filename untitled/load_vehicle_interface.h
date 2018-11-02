#ifndef LOAD_VEHICLE_INTERFACE_H
#define LOAD_VEHICLE_INTERFACE_H

#include <QWidget>

namespace Ui {
class load_vehicle_interface;
}

class load_vehicle_interface : public QWidget
{
    Q_OBJECT

public:
    explicit load_vehicle_interface(QWidget *parent = nullptr);
    ~load_vehicle_interface();

private:
    Ui::load_vehicle_interface *ui;
};

#endif // LOAD_VEHICLE_INTERFACE_H
