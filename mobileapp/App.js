import React, { useEffect, useState } from "react";
import { Text, SafeAreaView, View, ScrollView, StyleSheet } from "react-native";

const App = () => {
  //
  const [list, setList] = useState([]);

  const getAppointmentList = () => {
    fetch("http://127.0.0.1:8000/appointment", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        if (res) {
          setList(res.list);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getAppointmentList();
  }, []);

  return (
    <SafeAreaView>
      <Text style={styles.txtMain}>Appointment List {list.length} </Text>
      <ScrollView>
        {list.map((item, index) => {
          return (
            <View key={index}>
              <Text>{item.user_id}</Text>
            </View>
          );
        })}
      </ScrollView>
    </SafeAreaView>
  );
};

export default App;

const styles = StyleSheet.create({
  txtMain: {
    fontSize: 16,
    fontWeight: "bold",
  },
});
