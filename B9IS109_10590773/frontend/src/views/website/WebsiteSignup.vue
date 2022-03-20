<!--Signup template inhertited from website layout-->
<template>
  <div>
    <div
      class="alert alert-success text-center"
      role="alert"
      v-if="success_message != ''"
    >
      {{ success_message }}
    </div>
    <div class="container mt-5 d-flex">
      <div class="col-8">
        <img
          src="https://img.freepik.com/free-vector/drop-with-silhoutte-hands_24908-15743.jpg"
          alt=""
        />
      </div>
      <div class="col-4">
        <form @submit.prevent="SignupForAccount">
          <h2 class="text-danger">Signup new account</h2>
          <div class="form-group mb-2">
            <label for="exampleInputEmail1">Account Type</label>
            <div class="form-control">
              <input type="radio" value="accepter" v-model="account_type" />
              Accepter &nbsp;&nbsp;
              <input type="radio" value="donor" v-model="account_type" /> Donor
            </div>
          </div>
          <div class="form-group mb-2" v-show="account_type === 'donor'">
            <label for="exampleInputEmail1">Blood Group</label>
            <select class="form-control" v-model="blood_group">
              <option value="">-- Select Blood --</option>
              <option value="ap">A+ (A Positive)</option>
              <option value="ap">A- (A Negative)</option>
              <option value="op">O+ (A Positive)</option>
              <option value="op">O- (A Negative)</option>
              <option value="bp">B+ (A Positive)</option>
              <option value="bn">B- (A Negative)</option>
              <option value="abp">AB+ (AB Positive)</option>
              <option value="abn">AB- (AB Negative)</option>
            </select>
            <span class="text-danger" v-if="blood_group_err != ''">{{
              blood_group_err
            }}</span>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Full Name</label>
            <input type="text" class="form-control" v-model="full_name" />
            <span class="text-danger" v-if="full_name_err != ''">{{
              full_name_err
            }}</span>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Email</label>
            <input type="text" class="form-control" v-model="email" />
            <span class="text-danger" v-if="email_err != ''">{{
              email_err
            }}</span>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Contact</label>
            <input type="text" class="form-control" v-model="contact" />
            <span class="text-danger" v-if="contact_err != ''">{{
              contact_err
            }}</span>
          </div>
          <div class="form-group mb-2" v-show="account_type === 'donor'">
            <label for="exampleInputEmail1">Country</label>
            <select class="form-control" v-model="country">
              <option value="">-- Select Country --</option>
              <option value="Afganistan">Afghanistan</option>
              <option value="Albania">Albania</option>
              <option value="Algeria">Algeria</option>
              <option value="American Samoa">American Samoa</option>
              <option value="Andorra">Andorra</option>
              <option value="Angola">Angola</option>
              <option value="Anguilla">Anguilla</option>
              <option value="Antigua & Barbuda">Antigua & Barbuda</option>
              <option value="Argentina">Argentina</option>
              <option value="Armenia">Armenia</option>
              <option value="Aruba">Aruba</option>
              <option value="Australia">Australia</option>
              <option value="Austria">Austria</option>
              <option value="Azerbaijan">Azerbaijan</option>
              <option value="Bahamas">Bahamas</option>
              <option value="Bahrain">Bahrain</option>
              <option value="Bangladesh">Bangladesh</option>
              <option value="Barbados">Barbados</option>
              <option value="Belarus">Belarus</option>
              <option value="Belgium">Belgium</option>
              <option value="Belize">Belize</option>
              <option value="Benin">Benin</option>
              <option value="Bermuda">Bermuda</option>
              <option value="Bhutan">Bhutan</option>
              <option value="Bolivia">Bolivia</option>
              <option value="Bonaire">Bonaire</option>
              <option value="Bosnia & Herzegovina">Bosnia & Herzegovina</option>
              <option value="Botswana">Botswana</option>
              <option value="Brazil">Brazil</option>
              <option value="British Indian Ocean Ter">
                British Indian Ocean Ter
              </option>
              <option value="Brunei">Brunei</option>
              <option value="Bulgaria">Bulgaria</option>
              <option value="Burkina Faso">Burkina Faso</option>
              <option value="Burundi">Burundi</option>
              <option value="Cambodia">Cambodia</option>
              <option value="Cameroon">Cameroon</option>
              <option value="Canada">Canada</option>
              <option value="Canary Islands">Canary Islands</option>
              <option value="Cape Verde">Cape Verde</option>
              <option value="Cayman Islands">Cayman Islands</option>
              <option value="Central African Republic">
                Central African Republic
              </option>
              <option value="Chad">Chad</option>
              <option value="Channel Islands">Channel Islands</option>
              <option value="Chile">Chile</option>
              <option value="China">China</option>
              <option value="Christmas Island">Christmas Island</option>
              <option value="Cocos Island">Cocos Island</option>
              <option value="Colombia">Colombia</option>
              <option value="Comoros">Comoros</option>
              <option value="Congo">Congo</option>
              <option value="Cook Islands">Cook Islands</option>
              <option value="Costa Rica">Costa Rica</option>
              <option value="Cote DIvoire">Cote DIvoire</option>
              <option value="Croatia">Croatia</option>
              <option value="Cuba">Cuba</option>
              <option value="Curaco">Curacao</option>
              <option value="Cyprus">Cyprus</option>
              <option value="Czech Republic">Czech Republic</option>
              <option value="Denmark">Denmark</option>
              <option value="Djibouti">Djibouti</option>
              <option value="Dominica">Dominica</option>
              <option value="Dominican Republic">Dominican Republic</option>
              <option value="East Timor">East Timor</option>
              <option value="Ecuador">Ecuador</option>
              <option value="Egypt">Egypt</option>
              <option value="El Salvador">El Salvador</option>
              <option value="Equatorial Guinea">Equatorial Guinea</option>
              <option value="Eritrea">Eritrea</option>
              <option value="Estonia">Estonia</option>
              <option value="Ethiopia">Ethiopia</option>
              <option value="Falkland Islands">Falkland Islands</option>
              <option value="Faroe Islands">Faroe Islands</option>
              <option value="Fiji">Fiji</option>
              <option value="Finland">Finland</option>
              <option value="France">France</option>
              <option value="French Guiana">French Guiana</option>
              <option value="French Polynesia">French Polynesia</option>
              <option value="French Southern Ter">French Southern Ter</option>
              <option value="Gabon">Gabon</option>
              <option value="Gambia">Gambia</option>
              <option value="Georgia">Georgia</option>
              <option value="Germany">Germany</option>
              <option value="Ghana">Ghana</option>
              <option value="Gibraltar">Gibraltar</option>
              <option value="Great Britain">Great Britain</option>
              <option value="Greece">Greece</option>
              <option value="Greenland">Greenland</option>
              <option value="Grenada">Grenada</option>
              <option value="Guadeloupe">Guadeloupe</option>
              <option value="Guam">Guam</option>
              <option value="Guatemala">Guatemala</option>
              <option value="Guinea">Guinea</option>
              <option value="Guyana">Guyana</option>
              <option value="Haiti">Haiti</option>
              <option value="Hawaii">Hawaii</option>
              <option value="Honduras">Honduras</option>
              <option value="Hong Kong">Hong Kong</option>
              <option value="Hungary">Hungary</option>
              <option value="Iceland">Iceland</option>
              <option value="Indonesia">Indonesia</option>
              <option value="India">India</option>
              <option value="Iran">Iran</option>
              <option value="Iraq">Iraq</option>
              <option value="Ireland">Ireland</option>
              <option value="Isle of Man">Isle of Man</option>
              <option value="Israel">Israel</option>
              <option value="Italy">Italy</option>
              <option value="Jamaica">Jamaica</option>
              <option value="Japan">Japan</option>
              <option value="Jordan">Jordan</option>
              <option value="Kazakhstan">Kazakhstan</option>
              <option value="Kenya">Kenya</option>
              <option value="Kiribati">Kiribati</option>
              <option value="Korea North">Korea North</option>
              <option value="Korea Sout">Korea South</option>
              <option value="Kuwait">Kuwait</option>
              <option value="Kyrgyzstan">Kyrgyzstan</option>
              <option value="Laos">Laos</option>
              <option value="Latvia">Latvia</option>
              <option value="Lebanon">Lebanon</option>
              <option value="Lesotho">Lesotho</option>
              <option value="Liberia">Liberia</option>
              <option value="Libya">Libya</option>
              <option value="Liechtenstein">Liechtenstein</option>
              <option value="Lithuania">Lithuania</option>
              <option value="Luxembourg">Luxembourg</option>
              <option value="Macau">Macau</option>
              <option value="Macedonia">Macedonia</option>
              <option value="Madagascar">Madagascar</option>
              <option value="Malaysia">Malaysia</option>
              <option value="Malawi">Malawi</option>
              <option value="Maldives">Maldives</option>
              <option value="Mali">Mali</option>
              <option value="Malta">Malta</option>
              <option value="Marshall Islands">Marshall Islands</option>
              <option value="Martinique">Martinique</option>
              <option value="Mauritania">Mauritania</option>
              <option value="Mauritius">Mauritius</option>
              <option value="Mayotte">Mayotte</option>
              <option value="Mexico">Mexico</option>
              <option value="Midway Islands">Midway Islands</option>
              <option value="Moldova">Moldova</option>
              <option value="Monaco">Monaco</option>
              <option value="Mongolia">Mongolia</option>
              <option value="Montserrat">Montserrat</option>
              <option value="Morocco">Morocco</option>
              <option value="Mozambique">Mozambique</option>
              <option value="Myanmar">Myanmar</option>
              <option value="Nambia">Nambia</option>
              <option value="Nauru">Nauru</option>
              <option value="Nepal">Nepal</option>
              <option value="Netherland Antilles">Netherland Antilles</option>
              <option value="Netherlands">Netherlands (Holland, Europe)</option>
              <option value="Nevis">Nevis</option>
              <option value="New Caledonia">New Caledonia</option>
              <option value="New Zealand">New Zealand</option>
              <option value="Nicaragua">Nicaragua</option>
              <option value="Niger">Niger</option>
              <option value="Nigeria">Nigeria</option>
              <option value="Niue">Niue</option>
              <option value="Norfolk Island">Norfolk Island</option>
              <option value="Norway">Norway</option>
              <option value="Oman">Oman</option>
              <option value="Pakistan">Pakistan</option>
              <option value="Palau Island">Palau Island</option>
              <option value="Palestine">Palestine</option>
              <option value="Panama">Panama</option>
              <option value="Papua New Guinea">Papua New Guinea</option>
              <option value="Paraguay">Paraguay</option>
              <option value="Peru">Peru</option>
              <option value="Phillipines">Philippines</option>
              <option value="Pitcairn Island">Pitcairn Island</option>
              <option value="Poland">Poland</option>
              <option value="Portugal">Portugal</option>
              <option value="Puerto Rico">Puerto Rico</option>
              <option value="Qatar">Qatar</option>
              <option value="Republic of Montenegro">
                Republic of Montenegro
              </option>
              <option value="Republic of Serbia">Republic of Serbia</option>
              <option value="Reunion">Reunion</option>
              <option value="Romania">Romania</option>
              <option value="Russia">Russia</option>
              <option value="Rwanda">Rwanda</option>
              <option value="St Barthelemy">St Barthelemy</option>
              <option value="St Eustatius">St Eustatius</option>
              <option value="St Helena">St Helena</option>
              <option value="St Kitts-Nevis">St Kitts-Nevis</option>
              <option value="St Lucia">St Lucia</option>
              <option value="St Maarten">St Maarten</option>
              <option value="St Pierre & Miquelon">St Pierre & Miquelon</option>
              <option value="St Vincent & Grenadines">
                St Vincent & Grenadines
              </option>
              <option value="Saipan">Saipan</option>
              <option value="Samoa">Samoa</option>
              <option value="Samoa American">Samoa American</option>
              <option value="San Marino">San Marino</option>
              <option value="Sao Tome & Principe">Sao Tome & Principe</option>
              <option value="Saudi Arabia">Saudi Arabia</option>
              <option value="Senegal">Senegal</option>
              <option value="Seychelles">Seychelles</option>
              <option value="Sierra Leone">Sierra Leone</option>
              <option value="Singapore">Singapore</option>
              <option value="Slovakia">Slovakia</option>
              <option value="Slovenia">Slovenia</option>
              <option value="Solomon Islands">Solomon Islands</option>
              <option value="Somalia">Somalia</option>
              <option value="South Africa">South Africa</option>
              <option value="Spain">Spain</option>
              <option value="Sri Lanka">Sri Lanka</option>
              <option value="Sudan">Sudan</option>
              <option value="Suriname">Suriname</option>
              <option value="Swaziland">Swaziland</option>
              <option value="Sweden">Sweden</option>
              <option value="Switzerland">Switzerland</option>
              <option value="Syria">Syria</option>
              <option value="Tahiti">Tahiti</option>
              <option value="Taiwan">Taiwan</option>
              <option value="Tajikistan">Tajikistan</option>
              <option value="Tanzania">Tanzania</option>
              <option value="Thailand">Thailand</option>
              <option value="Togo">Togo</option>
              <option value="Tokelau">Tokelau</option>
              <option value="Tonga">Tonga</option>
              <option value="Trinidad & Tobago">Trinidad & Tobago</option>
              <option value="Tunisia">Tunisia</option>
              <option value="Turkey">Turkey</option>
              <option value="Turkmenistan">Turkmenistan</option>
              <option value="Turks & Caicos Is">Turks & Caicos Is</option>
              <option value="Tuvalu">Tuvalu</option>
              <option value="Uganda">Uganda</option>
              <option value="United Kingdom">United Kingdom</option>
              <option value="Ukraine">Ukraine</option>
              <option value="United Arab Erimates">United Arab Emirates</option>
              <option value="United States of America">
                United States of America
              </option>
              <option value="Uraguay">Uruguay</option>
              <option value="Uzbekistan">Uzbekistan</option>
              <option value="Vanuatu">Vanuatu</option>
              <option value="Vatican City State">Vatican City State</option>
              <option value="Venezuela">Venezuela</option>
              <option value="Vietnam">Vietnam</option>
              <option value="Virgin Islands (Brit)">
                Virgin Islands (Brit)
              </option>
              <option value="Virgin Islands (USA)">Virgin Islands (USA)</option>
              <option value="Wake Island">Wake Island</option>
              <option value="Wallis & Futana Is">Wallis & Futana Is</option>
              <option value="Yemen">Yemen</option>
              <option value="Zaire">Zaire</option>
              <option value="Zambia">Zambia</option>
              <option value="Zimbabwe">Zimbabwe</option>
            </select>
            <span class="text-danger" v-if="country_err != ''">{{
              country_err
            }}</span>
          </div>
          <div class="form-group mb-2 mt-2" v-show="account_type === 'donor'">
            <label for="exampleInputPassword1">City</label>
            <input type="text" class="form-control" v-model="city" />
            <span class="text-danger" v-if="city_err != ''">{{
              city_err
            }}</span>
          </div>
          <div class="form-group mb-2" v-show="account_type === 'donor'">
            <label for="exampleInputPassword1">Village</label>
            <input type="text" class="form-control" v-model="village" />
            <span class="text-danger" v-if="village_err != ''">{{
              village_err
            }}</span>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Gender</label>
            <select class="form-control" v-model="gender">
              <option value="male">I am male</option>
              <option value="female">I am female</option>
            </select>
          </div>
          <div class="form-group mb-2" v-show="account_type === 'donor'">
            <label for="exampleInputPassword1">Date of Birth</label>
            <input type="date" v-model="dob" class="form-control"/>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Passowrd</label>
            <input type="password" class="form-control" v-model="password" />
            <span class="text-danger" v-if="password_err != ''">{{
              password_err
            }}</span>
          </div>
          <div class="form-group mb-2">
            <label for="exampleInputPassword1">Confirm Passowrd</label>
            <input
              type="password"
              class="form-control"
              v-model="confirm_password"
            />
            <span class="text-danger" v-if="confirm_password_err != ''">{{
              confirm_password_err
            }}</span>
          </div>
          <button
            type="submit"
            class="btn btn-danger mt-3"
            style="float: right"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WebsiteSignup",
  data() {
    // componnets states
    return {
      account_type: "accepter",
      blood_group: "",
      full_name: "",
      email: "",
      contact: "",
      country: "",
      city: "",
      village: "",
      password: "",
      confirm_password: "",
      gender: "male",
      dob: "",

      blood_group_err: "",
      full_name_err: "",
      email_err: "",
      contact_err: "",
      country_err: "",
      city_err: "",
      village_err: "",
      password_err: "",
      confirm_password_err: "",
      gender_err: "male",
      dob_err: "",

      success_message: "",
    };
  },
  methods: {

    //  SignupForAccount to sent request to server to create new account
    SignupForAccount () {
      // field validation conditions
      if (this.account_type === "accepter") {
        if (this.full_name == "") {
          this.full_name_err = "Full name is required";
        }
        if (this.email == "") {
          this.email_err = "Email is required";
        }
        if (this.contact == "") {
          this.contact_err = "Contact is required";
        }
        if (this.password == "") {
          this.password_err = "Password is required";
        }
        if (this.confirm_password != this.password) {
          this.confirm_password_err = "Confirm password mismatch";
        }
        if (
          this.full_name != "" &&
          this.email != "" &&
          this.contact != "" &&
          this.password != "" &&
          this.confirm_password != "" &&
          this.password == this.confirm_password
        ) {
          var data = {
            email: this.email,
            user_type: this.account_type,
            full_name: this.full_name,
            contact: this.contact,
            gender: this.gender,
            password: this.password,
          };
          this.$axios
            .post(this.$base_url + "/api/signup/", data)
            .then((response) => {
              if (response.data.message) {
                this.success_message = response.data.message;
              }
              if (response.data.email) {
                this.email_err = response.data.email[0];
              }
              if (response.data.contact) {
                this.contact_err = response.data.contact[0];
              }
            });
        }
      } else {
        if (this.full_name == "") {
          this.full_name_err = "Full name is required";
        }
        if (this.email == "") {
          this.email_err = "Email is required";
        }
        if (this.contact == "") {
          this.contact_err = "Contact is required";
        }
        if (this.password == "") {
          this.password_err = "Password is required";
        }
        if (this.confirm_password != this.password) {
          this.confirm_password_err = "Confirm password mismatch";
        }
        if (this.country == "") {
          this.country_err = "Country is required";
        }
        if (this.city == "") {
          this.city_err = "City is required";
        }
        if (this.village == "") {
          this.village_err = "Village is required";
        }
        if (this.blood_group == "") {
          this.blood_group_err = "Blood group is required";
        }
        if (this.dob == "") {
          this.dob_err = "Date of birth is required";
        }

        if (
          this.full_name != "" &&
          this.email != "" &&
          this.contact != "" &&
          this.password != "" &&
          this.confirm_password != "" &&
          (this.password == this.confirm_password) &&
          this.country != "" &&
          this.city != "" &&
          this.village != "" &&
          this.blood_group != "" &&
          this.dob != ""
        ) {
          var data = {
            email: this.email,
            user_type: this.account_type,
            blood_group: this.blood_group,
            full_name: this.full_name,
            city: this.city,
            address: this.address,
            country: this.country,
            contact: this.contact,
            gender: this.gender,
            password: this.password,
            date_of_birth: this.dob,
          };
          this.$axios
            .post(this.$base_url + "/api/signup/", data)
            .then((response) => {
              if (response.data.message) {
                this.success_message = response.data.message;
              }
              if (response.data.email) {
                this.email_err = response.data.email;
              }
              if (response.data.contact) {
                this.contact_err = response.data.contact;
              }
            });
        }
      }
    },
  },
  mounted() {
    document.title = "Website | Signup";
  }
};
</script>